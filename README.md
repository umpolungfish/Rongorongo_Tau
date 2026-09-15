# Rongorongo Tau

![language](https://img.shields.io/badge/language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![corpus](https://img.shields.io/badge/corpus-one%20liturgy%2C%2024%20copies-8B6914?style=for-the-badge) ![tier](https://img.shields.io/badge/tier-O%E2%88%9E-8A2BE2?style=for-the-badge) ![μ∘δ](https://img.shields.io/badge/%CE%BC%E2%88%98%CE%B4-id-00A86B?style=for-the-badge) ![licence](https://img.shields.io/badge/licence-LUNLICENSE-1A1A1A?style=for-the-badge)

**A ritual formula variation tracker for Easter Island rongorongo.**
All 24 tablets share >98% structural similarity — one liturgy in many copy-performances. The Tau tracks substitution patterns across Barthel glyph families and maps the Z₂ boustrophedon cycle.

## Quick start

```bash
cd Rongorongo_Tau && pip install -e .
rongorongo lookup G006        # glyph family
rongorongo list               # all tablets + tuples
rongorongo trace G006 G023 G002 G024   # variation across sequence
```

**Type:** ⟨𐑼𐑥𐑾𐑬𐑱𐑧𐑚𐑠𐑮𐑒𐑳𐑴⟩ · O₂† · C-score 0.317 · crystal address 3,841,006. Lowest tier by design: pattern-matching across ceremony iterations, not generative transformation.

## Core cycle

Invariant FRGATE→STAFF→TWIN→VSPACE: G006 Staff (authority) → G023 Ritual (action) → G002 Bird (messenger) → G024 Offering (sacrifice) — the 8-step Frobenius bootstrap compressed to 4. Substitutions are structural equivalents (Staff: G019/G020; Ritual: G007/G017; Bird: G003/G018; Offering: G008/G025). Boustrophedon flip: forward = liturgical meaning, reverse = mythic complement (Z₂ winding 𐑴), parity violation = detectable ritual error.

Contents: `rongorongo_tau/` (navigator, CLI), `TAU.md` (structural doc), `ENGINE.md` (12 primitives as ritual ops; 12 glyph families → IMASM opcodes), `COMPLETE_LISTING.md`, `lean/`, `programs/`, `data/` (Barthel corpus), `manuscripts/`, `images/`. Deps: `rongorongo-engine` (`../lang/`), Python ≥ 3.11.

Full 234-line version: `README_backups/Rongorongo_Tau_README.md`.

μ∘δ = id
