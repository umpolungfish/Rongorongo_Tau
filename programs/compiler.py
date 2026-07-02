"""
IMASM compiler for Rongorongo glyph sequences.

Parses Barthel-numbered glyph sequences (the standard scholarly
transcription format) and emits IMASM opcodes. Each glyph is mapped
to its categorical operation via the primitives table.

The reverse boustrophedon reading order is encoded as alternating
line-direction flags, preserving the serpentine topology of the
original texts.

Barthel transcription format expected:
  Each glyph represented as a 3-digit Barthel number.
  Ligatures/compounds represented as hyphenated sequences (e.g., 200-300).
  Line breaks marked with newline.
  Tablet/side markers with > prefix (e.g., >A recto).
"""

from __future__ import annotations
from collections import defaultdict
from pathlib import Path
import re

from .primitives import PRIMITIVES, OPCODE_MAP, _SORTED_BARTHEL


def parse_glyph_sequence(text: str) -> list[tuple[str, dict]]:
    """Parse a string of Barthel-numbered glyphs into (barthel_id, prim) pairs.

    Handles:
      - Simple glyphs: '200'
      - Compounds: '200-300' → both glyphs extracted
      - Unknown glyphs: passed through as DATA with raw value
    """
    result = []
    # Split on whitespace, keep hyphenated compounds together
    tokens = text.strip().split()
    for token in tokens:
        token = token.strip('.,;:()[]{}')
        if not token:
            continue
        # Handle compounds: 200-300-100
        if '-' in token:
            parts = token.split('-')
            for part in parts:
                part = part.strip()
                if part in PRIMITIVES:
                    result.append((part, PRIMITIVES[part]))
                else:
                    result.append(('DATA', {'opcode': -1, 'mnemonic': 'RAW', 'operation': part, 'family': 'unknown'}))
        elif token in PRIMITIVES:
            result.append((token, PRIMITIVES[token]))
        else:
            # Try prefix match
            matched = False
            for bid in _SORTED_BARTHEL:
                if token.startswith(bid):
                    result.append((bid, PRIMITIVES[bid]))
                    matched = True
                    break
            if not matched:
                result.append(('DATA', {'opcode': -1, 'mnemonic': 'RAW', 'operation': token, 'family': 'unknown'}))
    return result


def compile_transcription(transcription_path: str | Path, verbose: bool = False) -> dict:
    """Compile a Barthel-format transcription to IMASM instruction stream.

    Returns dict with:
      tablets      — per-tablet results {name: {instructions, registers, line_count}}
      total_instructions
      total_registers
      tablet_count
      family_counts — opcode frequency by structural family
      direction_map — boustrophedon direction alternation
    """
    path = Path(transcription_path)
    if not path.exists():
        return {'error': f'File not found: {transcription_path}', 'tablets': {}}

    raw_text = path.read_text(encoding='utf-8', errors='ignore')

    # Split into tablets/sections
    tablets: dict[str, list[str]] = defaultdict(list)
    current_tablet = 'default'
    for line in raw_text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('>'):
            # Tablet/side marker
            current_tablet = line[1:].strip()
            continue
        tablets[current_tablet].append(line)

    results: dict[str, dict] = {}
    total_instructions = 0
    total_registers = 0
    family_counts: dict[str, int] = defaultdict(int)

    for tablet_name, lines in tablets.items():
        stream: list[str] = []
        reg = 0
        line_num = 0

        for line in lines:
            line_num += 1
            # Reverse boustrophedon: odd lines L→R, even lines R→L
            direction = 'L→R' if line_num % 2 == 1 else 'R→L'

            # If R→L, reverse the glyph order for compilation
            if direction == 'R→L':
                tokens = line.strip().split()
                tokens.reverse()
                line = ' '.join(tokens)

            stream.append(f'  ; LINE {line_num} [{direction}]')

            for barthel_id, prim in parse_glyph_sequence(line):
                if barthel_id == 'DATA':
                    stream.append(f'  DATA  | RAW_VAL {prim["operation"]}')
                else:
                    stream.append(f'  {hex(prim["opcode"])} | {prim["mnemonic"]:<8} %r{reg}')
                    family_counts[prim['family']] += 1
                    reg += 1

        results[tablet_name] = {
            'instructions': stream,
            'registers': reg,
            'line_count': line_num,
        }
        total_instructions += len([s for s in stream if not s.startswith('  ;')])
        total_registers += reg

    return {
        'tablets': results,
        'total_instructions': total_instructions,
        'total_registers': total_registers,
        'tablet_count': len(tablets),
        'family_counts': dict(family_counts),
    }


def write_log(result: dict, path: str | Path) -> None:
    """Write full compilation log."""
    path = Path(path)
    with path.open('w', encoding='utf-8') as f:
        for name, data in sorted(result.get('tablets', {}).items()):
            f.write(f'=== {name.upper()} ===\n')
            for instr in data['instructions']:
                f.write(instr + '\n')
            f.write(f'  -> {data["registers"]} registers, {data["line_count"]} lines\n\n')

        f.write(f'\n=== FAMILY COUNTS ===\n')
        for family, count in sorted(result.get('family_counts', {}).items()):
            f.write(f'  {family:<16} {count}\n')

        f.write(f'\nTotal instructions: {result.get("total_instructions", 0)}\n')
        f.write(f'Total registers:    {result.get("total_registers", 0)}\n')
        f.write(f'Tablet count:       {result.get("tablet_count", 0)}\n')

