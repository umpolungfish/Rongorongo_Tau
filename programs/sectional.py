"""
Sectional / topological analysis of Rongorongo tablet structure.

Analyzes text at three scales:
  1. Glyph-level: individual opcode frequencies and patterns
  2. Line-level: boustrophedon reversal structure, line density
  3. Tablet-level: cross-tablet structural comparison

The sectional analysis reveals how the undeciphered text is organized
hierarchically — which glyph families cluster together, how lines
alternate direction, and whether different tablets share structural
patterns (suggesting shared genres or formulaic content).
"""

from __future__ import annotations
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from pathlib import Path

from .primitives import FAMILY_TO_PRIMITIVE, OPCODE_MAP, PRIMITIVES
from .runtime import RuntimeState, execute_stream


@dataclass
class SectionProfile:
    """Structural profile of one text section."""
    name: str
    glyph_count: int = 0
    line_count: int = 0
    family_distribution: Counter = field(default_factory=Counter)
    opcode_distribution: Counter = field(default_factory=Counter)
    direction_pattern: list[str] = field(default_factory=list)
    frobenius_closure: float = 0.0  # 0.0 to 1.0
    dominant_family: str = ''
    dominant_opcode: str = ''


def profile_tablet(state: RuntimeState) -> SectionProfile:
    """Build a structural profile for one tablet's runtime state."""
    profile = SectionProfile(name=state.tablet_name)
    profile.line_count = state.line_number
    profile.direction_pattern.append(state.direction)

    regs = state.registers
    profile.glyph_count = len(regs)

    for reg in regs:
        profile.family_distribution[reg.family] += 1
        profile.opcode_distribution[reg.mnemonic] += 1

    if profile.family_distribution:
        profile.dominant_family = profile.family_distribution.most_common(1)[0][0]

    if profile.opcode_distribution:
        profile.dominant_opcode = profile.opcode_distribution.most_common(1)[0][0]

    # Frobenius closure score
    gate_ops = profile.opcode_distribution.get('GATE', 0) + profile.opcode_distribution.get('BRANCH', 0) + profile.opcode_distribution.get('RIFT', 0)
    close_ops = profile.opcode_distribution.get('END', 0) + profile.opcode_distribution.get('CYCLE', 0) + profile.opcode_distribution.get('MERGE', 0)
    total_frob = gate_ops + close_ops
    if total_frob > 0:
        profile.frobenius_closure = close_ops / total_frob

    return profile


def profile_corpus(states: dict[str, RuntimeState]) -> dict[str, SectionProfile]:
    """Profile all tablets in a corpus."""
    return {name: profile_tablet(state) for name, state in states.items()}


def cross_tablet_comparison(profiles: dict[str, SectionProfile]) -> str:
    """Compare structural profiles across all tablets."""
    lines = []
    lines.append('=== CROSS-TABLET STRUCTURAL COMPARISON ===')
    lines.append('')

    # Header
    lines.append(f'{"Tablet":<20} {"Glyphs":>7} {"Lines":>6} {"Frob":>6} {"Dominant Family":<16} {"Dominant Op"}')
    lines.append('-' * 80)

    for name, prof in sorted(profiles.items()):
        dom_fam_prim = FAMILY_TO_PRIMITIVE.get(prof.dominant_family, '?')
        lines.append(
            f'{name:<20} {prof.glyph_count:>7} {prof.line_count:>6} '
            f'{prof.frobenius_closure:>6.3f} {dom_fam_prim} {prof.dominant_family:<14} {prof.dominant_opcode}'
        )

    # Aggregate family distribution
    lines.append('')
    lines.append('--- Aggregate Family Distribution ---')
    agg_families: Counter = Counter()
    for prof in profiles.values():
        agg_families.update(prof.family_distribution)
    total = sum(agg_families.values())
    for fam, count in agg_families.most_common():
        prim = FAMILY_TO_PRIMITIVE.get(fam, '?')
        pct = 100 * count / total if total > 0 else 0
        lines.append(f'  {prim} {fam:<16} {count:>6} ({pct:.1f}%)')

    # Similarity clustering
    lines.append('')
    lines.append('--- Tablet Similarity (by family distribution) ---')
    tablet_names = sorted(profiles.keys())
    for i, name_a in enumerate(tablet_names):
        for name_b in tablet_names[i+1:]:
            sim = _cosine_similarity(
                profiles[name_a].family_distribution,
                profiles[name_b].family_distribution,
            )
            if sim > 0.5:
                lines.append(f'  {name_a} ↔ {name_b}: {sim:.3f}')

    return '\n'.join(lines)


def _cosine_similarity(a: Counter, b: Counter) -> float:
    """Cosine similarity between two Counters."""
    all_keys = set(a.keys()) | set(b.keys())
    dot = sum(a.get(k, 0) * b.get(k, 0) for k in all_keys)
    norm_a = sum(v**2 for v in a.values()) ** 0.5
    norm_b = sum(v**2 for v in b.values()) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def write_sectional_report(
    profiles: dict[str, SectionProfile],
    path: str | Path,
    comparison: str = '',
) -> None:
    """Write full sectional analysis report."""
    path = Path(path)
    with path.open('w', encoding='utf-8') as f:
        f.write('=== RONGORONGO SECTIONAL ANALYSIS ===\n\n')
        f.write(f'Tablets analyzed: {len(profiles)}\n')
        total_glyphs = sum(p.glyph_count for p in profiles.values())
        f.write(f'Total glyphs: {total_glyphs}\n\n')

        for name, prof in sorted(profiles.items()):
            f.write(f'--- {name} ---\n')
            f.write(f'  Glyphs: {prof.glyph_count}\n')
            f.write(f'  Lines:  {prof.line_count}\n')
            f.write(f'  Frobenius closure: {prof.frobenius_closure:.3f}\n')
            f.write(f'  Dominant family: {prof.dominant_family}\n')
            f.write(f'  Family distribution:\n')
            for fam, count in prof.family_distribution.most_common():
                prim = FAMILY_TO_PRIMITIVE.get(fam, '?')
                pct = 100 * count / prof.glyph_count if prof.glyph_count > 0 else 0
                f.write(f'    {prim} {fam:<16} {count:>5} ({pct:.1f}%)\n')
            f.write('\n')

        if comparison:
            f.write(comparison)

