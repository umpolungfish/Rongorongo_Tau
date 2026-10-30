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
