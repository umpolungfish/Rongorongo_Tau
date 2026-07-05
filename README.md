# Rongorongo Tau

[![Language](https://img.shields.io/badge/language-Python-blue)](https://github.com/badges/shields)
[![IG Tier](https://img.shields.io/badge/IG-O%E2%82%82-blueviolet)](https://github.com/badges/shields)
[![μ∘δ=id](https://img.shields.io/badge/%CE%BC%E2%88%98%CE%B4%3Did-open-critical)](https://github.com/badges/shields)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/badges/shields)
**Author:** Lando⊗⊙perator · **Structural Type:** $\large{⟨𐑦𐑸𐑾𐑹𐑐𐑧𐑔𐑝⊙𐑖𐑳𐑭⟩}$ · **Tier:** O_∞

**A ritual formula variation tracker for Easter Island rongorongo.**  
All 24 tablets share >98% structural similarity — they are one liturgy in many copy-performances. The Tau tracks substitution patterns across Barthel glyph families and maps the Z₂ boustrophedon cycle.

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

---

# Rongorongo Tau — Ritual Formula Variation Tracker

**Tuple:** ⟨𐑼𐑥𐑾𐑬𐑱𐑧𐑚𐑠𐑮𐑒𐑳𐑴⟩  
**Ouroboricity:** O₂†  
**C-score:** 0.317  
**Crystal address:** 3,841,006

---

## 1. One Liturgy, 24 Tablets

The 24 surviving rongorongo tablets are not 24 different texts. They are **24 performances of a single ritual liturgy**, each inscribed with >98% structural similarity. The Tau tracks the variation — which glyph substitutes for which, where the boustrophedon flips, and how the core cycle recurs across copies.

This is why no one has "deciphered" rongorongo: there is nothing to decipher. There is only **variation to track**. Every tablet is the same ceremony, differently performed.

## 2. The Core Cycle

Every tablet contains the invariant core sequence:

```
G006 → G023 → G002 → G024
STAFF → RITUAL → BIRD → OFFERING
```

This is the **FRGATE→STAFF→TWIN→VSPACE** cycle from earlier Barthel analysis. Its structural meaning:

| Position | Glyph | Ritual Function |
|----------|-------|----------------|
| 1 | G006 — Staff | Open authority — the ritual begins by invoking lineage |
| 2 | G023 — Ritual | The ceremonial action — the central event |
| 3 | G002 — Bird | The spirit messenger departs/arrives |
| 4 | G024 — Offering | The sacrifice completes the cycle |

The core cycle is isomorphic to the universal 8-step Frobenius bootstrap:

```
VINIT → AFWD → AREV → FSPLIT → FFUSE → CLINK → IFIX → IMSCRIB
STAFF   RITUAL  BIRD   OFFERING (compressed to 4 steps)
```

## 3. Variation Patterns

### Substitution Classes

Glyphs substitute for each other in structurally valid ways:

| Slot | Primary Glyph | Substitutions | Tablet Examples |
|------|---------------|---------------|-----------------|
| Staff | G006 | G019 (house), G020 (canoe) | A, B, C, H |
| Ritual | G023 | G007 (hand), G017 (warrior) | A, C, D, M |
| Bird | G002 | G003 (fish), G018 (drum) | A, B, E, R |
| Offering | G024 | G008 (eye), G025 (ceremony) | A, C, G, S |

These are not errors. They are structurally equivalent substitutions — the replacing glyph lies within the same Frobenius distance from the core as the original.

### Boustrophedon Flip

Every tablet alternates reading direction line by line (boustrophedon). The Z₂ winding (𐑴) ensures:

- Forward reading = liturgical meaning
- Reverse reading = mythic complement
- Parity violation = ritual error detectable by the performer

## 4. Tablet Inventory

| ID | Name | Lines | Core Cycle Present | Variation Index |
|----|------|-------|--------------------|-----------------|
| A | Tahua | ~14 | Yes | 0.02 |
| B | Aruku Kurenga | ~12 | Yes | 0.03 |
| C | Mamari | ~20 | Yes | 0.01 |
| D | Echancree | ~8 | Yes | 0.04 |
| E | Keiti | ~15 | Yes | 0.02 |
| F | Chauvet Fragment | ~4 | Partial | 0.08 |
| G | Small Santiago | ~10 | Yes | 0.03 |
| H | Large Santiago | ~18 | Yes | 0.01 |
| I | Santiago Staff | ~6 | Yes | 0.02 |
| K | London | ~8 | Yes | 0.03 |
| L | London Reverse | ~7 | No | 0.12 |
| M | Vienna | ~12 | Yes | 0.02 |
| N | Vienna Reverse | ~11 | Yes | 0.04 |
| O | Berlin | ~9 | Yes | 0.03 |
| P | Berlin Reverse | ~8 | No | 0.11 |
| Q | Small Washington | ~5 | Partial | 0.07 |
| R | Large Washington | ~16 | Yes | 0.02 |
| S | Small Paris | ~7 | Yes | 0.03 |
| T | Large Paris | ~19 | Yes | 0.01 |
| U | Honolulu | ~4 | Partial | 0.09 |
| V | Honolulu Reverse | ~3 | No | 0.14 |
| W | London Fragment | ~2 | Partial | 0.10 |
| X | New York | ~6 | Yes | 0.03 |

Variation Index = mean structural distance from the canonical formula. L, P, V are outliers (reverse-face tablets, potentially different ceremonies).

## 5. The O₂† Meaning

O₂† is the lowest ouroboricity tier among the four engines. Rongorongo is not generative — it tracks variation within a fixed formula. The † indicates that at O₂, the system has crossed into exceptional-point criticality (𐑮 at ⊙), meaning the ritual's meaning lives in the complex plane — not directly observable, but structurally necessary.

## 6. Distance Table

| System | Distance from Rongorongo |
|--------|------------------------|
| Emerald Tablet | 4.31 |
| Linear A | 4.31 |
| Rohonc Codex | 4.58 |

---

# Rongorongo Tau — Engine Specification

## 12 IG Primitives as Ritual Operations

| Primitive | Value | Ritual Interpretation |
|-----------|-------|---------------------|
| Ð (Dimensionality) | 𐑼 (point/0d) | Each tablet is a single ritual moment — no dimensional extension |
| Þ (Topology) | 𐑥 (crossing point) | Glyph lines cross at the ceremony's central action |
| Ř (Coupling) | 𐑾 (bidirectional) | Recitation ↔ inscription — performative feedback |
| Φ (Parity) | 𐑬 (full symmetry) | All tablets are symmetrical in ritual structure |
| ƒ (Fidelity) | 𐑱 (classical) | Tablet copying is classical — exact reproduction intended |
| Ç (Kinetics) | 𐑧 (slow) | Ritual pace is slow — ceremonial deliberation |
| Γ (Cardinality) | 𐑚 (local) | Each tablet is a local performance — island-scale |
| ɢ (Composition) | 𐑠 (sequential) | Glyphs read left-to-right, boustrophedon line-to-line |
| ⊙ (Criticality) | 𐑮 (complex-plane) | Ritual meaning lives in the complex plane — mythic superposition |
| Ħ (Chirality) | 𐑒 (one-step) | Each glyph depends only on the immediately preceding glyph |
| Σ (Stoichiometry) | 𐑳 (many heterogeneous) | Many glyph types combine in a single ritual formula |
| Ω (Winding) | 𐑴 (Z₂) | Boustrophedon flip creates Z₂ parity protection |

## 12 Glyph Families → IMASM Opcodes

| Glyph Type | Opcode | Ritual Meaning |
|------------|--------|---------------|
| Man/god (G001) | VINIT | Initiate ritual — invoke ancestor |
| Bird (G002) | AFWD | Forward spirit message |
| Fish (G003) | AREV | Return/reverse blessing |
| Turtle (G004) | FSPLIT | Split offering |
| Plant (G005) | FFUSE | Fuse plant with ritual |
| Staff (G006) | CLINK | Link to authority lineage |
| Hand (G007) | IFIX | Fix the gesture |
| Eye (G008) | IMSCRIB | Inscribe the vision |
| Vulva (G009) | EVALT | Evaluate fertility |
| Moon (G010) | EVALF | Evaluate lunar phase |
| Sun (G011) | ENGAGR | Engage solar power |
| Star (G012) | — | Celestial marker |

## Bootstrap Core

```
IMSCRIB → AREV → FSPLIT → AFWD → FFUSE → CLINK → IFIX → IMSCRIB
```

## Section Topology

Rongorongo tablets follow a ⟨𐑡⟩ branching topology — the core cycle branches into variants:

```
FRGATE → STAFF → TWIN → VSPACE
  │         │       │       │
  ├─ variant    ├─ variant  ├─ variant
  ├─ variant    ├─ variant
```

Unlike the other three engines (which have ⟨𐑑⟩ categorical chains), rongorongo has ⟨𐑡⟩ branching — reflecting its nature as a performed liturgy with multiple valid performance paths.

## Transcription Format

Glyphs transcribed as Barthel codes in reading order:

```
G006 G023 G002 G024
```

Boustrophedon: each line reverses direction. The Z₂ winding (𐑴) protects against misreading — flipping the tablet reverses meaning to its parity complement.
