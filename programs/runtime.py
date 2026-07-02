"""
IMASM runtime for compiled Rongorongo glyph streams.

Executes the opcode stream produced by the compiler. Each opcode
advances a linear register tape, with the 12 structural families
interacting according to IG algebraic rules.

Key runtime features:
  - Linear register allocation (monotonic append-only)
  - Family-stack tracking (which primitive families are active)
  - Boustrophedon reversal accounting
  - Frobenius closure check: every δ (FSPLIT analog) must have μ (FFUSE)
"""

from __future__ import annotations
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from .primitives import OPCODE_MAP, FAMILY_TO_PRIMITIVE


@dataclass
class Register:
    index: int
    opcode: int
    mnemonic: str
    family: str
    primitive: str  # IG primitive letter


@dataclass
class RuntimeState:
    registers: list[Register] = field(default_factory=list)
    family_stack: list[str] = field(default_factory=list)
    direction: str = 'L→R'
    line_number: int = 0
    tablet_name: str = ''
    errors: list[str] = field(default_factory=list)

    def push(self, opcode: int, mnemonic: str, family: str) -> None:
        reg = Register(
            index=len(self.registers),
            opcode=opcode,
            mnemonic=mnemonic,
            family=family,
            primitive=FAMILY_TO_PRIMITIVE.get(family, '?'),
        )
        self.registers.append(reg)
        self.family_stack.append(family)

    def reset(self) -> None:
        self.registers.clear()
        self.family_stack.clear()
        self.errors.clear()


def execute_stream(
    instructions: list[str],
    tablet_name: str = '',
    check_frobenius: bool = True,
) -> RuntimeState:
    """Execute an IMASM instruction stream for one tablet."""
    state = RuntimeState(tablet_name=tablet_name)

    for line in instructions:
        line = line.strip()
        if not line or line.startswith(';'):
            # Comment line — may contain direction info
            if 'R→L' in line:
                state.direction = 'R→L'
            elif 'L→R' in line:
                state.direction = 'L→R'
            continue
        if 'DATA' in line:
            continue

        # Parse: 0x14 | FRGATE   %r7
        parts = line.split('|')
        if len(parts) < 2:
            continue

        opcode_part = parts[0].strip()
        rest = parts[1].strip()

        try:
            opcode = int(opcode_part, 16)
        except ValueError:
            state.errors.append(f'Bad opcode: {opcode_part}')
            continue

        mnemonic = rest.split('%')[0].strip() if '%' in rest else rest.strip()

        # Look up family from opcode
        family = 'unknown'
        if opcode in OPCODE_MAP:
            barthel_id, _ = OPCODE_MAP[opcode]
            from .primitives import PRIMITIVES
            family = PRIMITIVES.get(barthel_id, {}).get('family', 'unknown')

        state.push(opcode, mnemonic, family)

    # Frobenius check
    if check_frobenius:
        _frobenius_check(state)

    return state


def _frobenius_check(state: RuntimeState) -> None:
    """Check Frobenius closure: every opening operation should have closure.

    In the IG framework: μ∘δ = id. For Rongorongo, we check:
      - GATE (0x24) should have corresponding END (0x33) or CYCLE (0x30)
      - BRANCH (0x07) should have corresponding MERGE (0x26)
      - RIFT (0x27) should have corresponding MERGE (0x26)
    """
    opcodes = [r.opcode for r in state.registers]
    gate_count = opcodes.count(0x24)
    end_count = opcodes.count(0x33)
    cycle_count = opcodes.count(0x30)
    closure_count = end_count + cycle_count

    branch_count = opcodes.count(0x07)
    merge_count = opcodes.count(0x26)
    rift_count = opcodes.count(0x27)

    if gate_count > closure_count:
        state.errors.append(
            f'FROBENIUS GAP: {gate_count} GATE ops vs {closure_count} END/CYCLE closures '
            f'(δ over μ by {gate_count - closure_count})'
        )

    if branch_count + rift_count > merge_count:
        state.errors.append(
            f'FROBENIUS GAP: {branch_count + rift_count} splits vs {merge_count} merges '
            f'(δ over μ by {branch_count + rift_count - merge_count})'
        )


def execute_corpus(compiled: dict, check_frobenius: bool = True) -> dict[str, RuntimeState]:
    """Execute all tablets in a compiled corpus."""
    states = {}
    for name, data in compiled.get('tablets', {}).items():
        states[name] = execute_stream(
            data['instructions'],
            tablet_name=name,
            check_frobenius=check_frobenius,
        )
    return states


def summary(states: dict[str, RuntimeState]) -> str:
    """Generate a human-readable summary of all runtime states."""
    lines = []
    total_regs = 0
    total_errors = 0
    family_totals: Counter = Counter()

    for name, state in states.items():
        lines.append(f'{name}: {len(state.registers)} ops, {len(state.errors)} errors')
        total_regs += len(state.registers)
        total_errors += len(state.errors)
        for r in state.registers:
            family_totals[r.family] += 1

    lines.append(f'\nTotal: {total_regs} ops across {len(states)} tablets')
    lines.append(f'Errors: {total_errors}')
    lines.append(f'\nFamily distribution:')
    for fam, count in family_totals.most_common():
        prim = FAMILY_TO_PRIMITIVE.get(fam, '?')
        lines.append(f'  {prim} {fam:<16} {count:>6} ({100*count/total_regs:.1f}%)')

    return '\n'.join(lines)

