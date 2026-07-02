"""
Callgraph construction and analysis for Rongorongo IMASM streams.

Constructs a directed graph where nodes are registers (opcode instances)
and edges represent sequential flow, with special edges for:
  - Boustrophedon reversals (direction changes between lines)
  - Frobenius δ/μ pairs (GATE→END, BRANCH→MERGE, RIFT→MERGE)
  - Family transitions (which primitive families follow which)

The callgraph reveals the structural topology of the undeciphered text:
repetition patterns, cyclic structures, and the distribution of
categorical operations across the 12 primitive families.
"""

from __future__ import annotations
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from pathlib import Path

from .primitives import OPCODE_MAP, FAMILY_TO_PRIMITIVE, PRIMITIVES
from .runtime import RuntimeState, Register


@dataclass
class CallGraph:
    """Directed graph of opcode transitions."""
    # Adjacency: family_transitions[src_family][dst_family] = count
    family_transitions: dict[str, Counter] = field(default_factory=dict)
    # Opcode-level transitions
    opcode_transitions: dict[int, Counter] = field(default_factory=dict)
    # Special edge types
    reversal_edges: int = 0
    frobenius_edges: int = 0
    # Node counts per family
    family_nodes: Counter = field(default_factory=Counter)
    # Tablet boundaries
    tablet_names: list[str] = field(default_factory=list)
    # Line structure
    lines_per_tablet: dict[str, int] = field(default_factory=dict)
    # Boustrophedon pattern
    direction_sequence: list[str] = field(default_factory=list)


def build_callgraph(states: dict[str, RuntimeState]) -> CallGraph:
    """Build a callgraph from executed runtime states."""
    cg = CallGraph()

    for tablet_name, state in states.items():
        cg.tablet_names.append(tablet_name)
        cg.lines_per_tablet[tablet_name] = state.line_number
        cg.direction_sequence.append(state.direction)

        regs = state.registers
        for i, reg in enumerate(regs):
            cg.family_nodes[reg.family] += 1

            if i + 1 < len(regs):
                nxt = regs[i + 1]
                src_fam = reg.family
                dst_fam = nxt.family

                if src_fam not in cg.family_transitions:
                    cg.family_transitions[src_fam] = Counter()
                cg.family_transitions[src_fam][dst_fam] += 1

                if reg.opcode not in cg.opcode_transitions:
                    cg.opcode_transitions[reg.opcode] = Counter()
                cg.opcode_transitions[reg.opcode][nxt.opcode] += 1

                # Frobenius edges
                if _is_frobenius_pair(reg, nxt):
                    cg.frobenius_edges += 1

    return cg


def _is_frobenius_pair(a: Register, b: Register) -> bool:
    """Check if two consecutive registers form a Frobenius δ/μ pair."""
    # GATE (0x24) → END (0x33) or CYCLE (0x30)
    if a.opcode == 0x24 and b.opcode in (0x30, 0x33):
        return True
    # BRANCH (0x07) or RIFT (0x27) → MERGE (0x26)
    if a.opcode in (0x07, 0x27) and b.opcode == 0x26:
        return True
    return False


def callgraph_report(cg: CallGraph) -> str:
    """Generate a human-readable callgraph report."""
    lines = []
    lines.append('=== RONGORONGO CALLGRAPH ANALYSIS ===')
    lines.append(f'Tablets analyzed: {len(cg.tablet_names)}')
    lines.append(f'Total direction reversals: {len(cg.direction_sequence)}')
    lines.append(f'Frobenius edge pairs: {cg.frobenius_edges}')
    lines.append('')

    lines.append('--- Family Node Distribution ---')
    total_nodes = sum(cg.family_nodes.values())
    for fam, count in cg.family_nodes.most_common():
        prim = FAMILY_TO_PRIMITIVE.get(fam, '?')
        pct = 100 * count / total_nodes if total_nodes > 0 else 0
        lines.append(f'  {prim} {fam:<16} {count:>5} ({pct:.1f}%)')

    lines.append('')
    lines.append('--- Family Transition Matrix (top 10) ---')
    all_transitions = []
    for src, dsts in cg.family_transitions.items():
        for dst, count in dsts.items():
            all_transitions.append((src, dst, count))
    all_transitions.sort(key=lambda x: x[2], reverse=True)

    for src, dst, count in all_transitions[:10]:
        prim_src = FAMILY_TO_PRIMITIVE.get(src, '?')
        prim_dst = FAMILY_TO_PRIMITIVE.get(dst, '?')
        lines.append(f'  {prim_src} {src:<14} → {prim_dst} {dst:<14} : {count}')

    lines.append('')
    lines.append('--- Most Common Opcode Transitions (top 10) ---')
    op_transitions = []
    for src_op, dsts in cg.opcode_transitions.items():
        for dst_op, count in dsts.items():
            src_info = OPCODE_MAP.get(src_op, ('???', '???'))
            dst_info = OPCODE_MAP.get(dst_op, ('???', '???'))
            op_transitions.append((src_op, dst_op, src_info[1], dst_info[1], count))
    op_transitions.sort(key=lambda x: x[4], reverse=True)

    for src_op, dst_op, src_mne, dst_mne, count in op_transitions[:10]:
        lines.append(f'  {src_mne:<8} → {dst_mne:<8} : {count}')

    return '\n'.join(lines)


def write_callgraph_dot(cg: CallGraph, path: str | Path) -> None:
    """Write callgraph in Graphviz DOT format for visualization."""
    path = Path(path)
    with path.open('w', encoding='utf-8') as f:
        f.write('digraph Rongorongo {\n')
        f.write('  rankdir=LR;\n')
        f.write('  node [shape=box, style=rounded];\n')

        # Nodes: families
        for fam in cg.family_nodes:
            prim = FAMILY_TO_PRIMITIVE.get(fam, '?')
            count = cg.family_nodes[fam]
            f.write(f'  "{fam}" [label="{prim} {fam}\\n{count} ops"];\n')

        # Edges: family transitions
        for src, dsts in cg.family_transitions.items():
            for dst, count in dsts.items():
                f.write(f'  "{src}" -> "{dst}" [label="{count}", penwidth={max(1, count/5)}];\n')

        f.write('}\n')

