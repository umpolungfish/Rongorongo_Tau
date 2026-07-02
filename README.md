# Rongorongo Tau

**A ritual formula variation tracker for Easter Island rongorongo.**  
All 24 tablets share >98% structural similarity — they are one liturgy in many copy-performances. The Tau tracks substitution patterns across Barthel glyph families and maps the Z₂ boustrophedon cycle.

**Author:** Lando⊗⊙perator

## Quick Start

```bash
cd Rongorongo_Tau
pip install -e .

# Look up a glyph family
rt lookup G006

# List all tablets with their tuples
rt list

# Trace variation across a glyph sequence
rt trace G006 G023 G002 G024
```

## Structural Type

| Property | Value |
|----------|-------|
| Tuple | ⟨𐑼𐑥𐑾𐑬𐑱𐑧𐑚𐑠𐑮𐑒𐑳𐑴⟩ |
| Tier | O₂† |
| C-score | 0.317 |

Lowest structural tier — designed for pattern-matching across iterations of a single ceremony, not for generative transformation.

## Contents

- `rongorongo_tau/` — Python package (navigator, CLI)
- `TAU.md` — Definitive structural document
- `ENGINE.md` — Engine specification
- `COMPLETE_LISTING.md` — Full glyph and tablet inventory
- `lean/` — Lean 4 companion files
- `programs/` — Engine source code
- `data/` — Barthel transcription corpus
- `manuscripts/` — Source tablet photographs and facsimiles
- `images/` — Variation diagrams and cycle maps

## Core Cycle

The invariant FRGATE→STAFF→TWIN→VSPACE core cycle recurs across all tablets:

| Glyph | Code | Role |
|-------|------|------|
| Staff | G006 | Authority marker |
| Ritual | G023 | Ceremonial action |
| Bird | G002 | Spirit messenger |
| Offering | G024 | Sacrificial logic |

## Dependencies

- `rongorongo-engine` (from `../lang/rongorongo-engine`)
- Python ≥ 3.11
