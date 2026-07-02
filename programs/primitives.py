"""
The twelve Barthel glyph families as IG categorical opcodes.

Barthel's ~120 basic glyph types are organized into 12 structural families
corresponding to the 12 IG primitives. The mapping is structural: each
Barthel glyph family encodes a specific categorical operation.

Rongorongo is a mixed logographic-syllabic system. The glyphs are
stylized outlines of living organisms and geometric forms, organized
into compounds via ligature and affixation. The reading order is reverse
boustrophedon (alternating direction, bottom-to-top).

Barthel numbering scheme:
  000-099 : Geometric / abstract
  100-199 : Anthropomorphic (basic)
  200-299 : Anthropomorphic (with attributes)
  300-399 : Birds
  400-499 : Fish and marine life
  500-599 : Plants and vegetation
  600-699 : Artifacts and implements
  700-799 : Compounds and ligatures
  800-899 : Additional compounds
  900-999 : Unclassified / variants
"""

PRIMITIVES: dict[str, dict] = {
    # ── DIMENSIONALITY (D) ── Domain / cosmic structure ──
    # Barthel 001-009: Geometric foundations
    '001': {'opcode': 0x0, 'mnemonic': 'VSPACE',  'operation': 'Cosmic void / domain boundary',     'family': 'dimensionality', 'barthel': 'Straight vertical line'},
    '002': {'opcode': 0x1, 'mnemonic': 'HSPACE',  'operation': 'Horizon / ground line',             'family': 'dimensionality', 'barthel': 'Straight horizontal line'},
    '003': {'opcode': 0x2, 'mnemonic': 'DSPACE',  'operation': 'Diagonal / depth dimension',        'family': 'dimensionality', 'barthel': 'Diagonal line'},
    '004': {'opcode': 0x3, 'mnemonic': 'DOT',     'operation': 'Point / origin / seed',             'family': 'dimensionality', 'barthel': 'Dot or small circle'},
    '005': {'opcode': 0x4, 'mnemonic': 'CROSS',   'operation': 'Intersection / axis mundi',         'family': 'dimensionality', 'barthel': 'Cross or X shape'},
    '006': {'opcode': 0x5, 'mnemonic': 'STAR',    'operation': 'Radiant point / celestial body',    'family': 'dimensionality', 'barthel': 'Star or asterisk'},

    # ── TOPOLOGY (T) ── Connection / containment ──
    # Barthel 010-019: Connection patterns
    '010': {'opcode': 0x6, 'mnemonic': 'LINK',    'operation': 'Connection / path',                 'family': 'topology',       'barthel': 'Joined lines or chain'},
    '011': {'opcode': 0x7, 'mnemonic': 'BRANCH',  'operation': 'Branching / divergence',            'family': 'topology',       'barthel': 'Forked line or Y-shape'},
    '012': {'opcode': 0x8, 'mnemonic': 'ENCLOSE', 'operation': 'Containment / enclosure',           'family': 'topology',       'barthel': 'Circle or enclosing curve'},
    '013': {'opcode': 0x9, 'mnemonic': 'SPIRAL',  'operation': 'Winding / recursive structure',     'family': 'topology',       'barthel': 'Spiral form'},
    '014': {'opcode': 0xA, 'mnemonic': 'KNOT',    'operation': 'Irreducible entanglement',          'family': 'topology',       'barthel': 'Interlocking curves'},

    # ── COUPLING (R) ── Relationship / orientation ──
    # Barthel 100-119: Basic human figures in relation
    '100': {'opcode': 0xB, 'mnemonic': 'STAND',   'operation': 'Upright figure / presence',        'family': 'coupling',       'barthel': 'Standing human figure'},
    '101': {'opcode': 0xC, 'mnemonic': 'FACE',    'operation': 'Confrontation / address',           'family': 'coupling',       'barthel': 'Two figures facing'},
    '102': {'opcode': 0xD, 'mnemonic': 'TURN',    'operation': 'Reversal / turning away',           'family': 'coupling',       'barthel': 'Figures back-to-back'},
    '103': {'opcode': 0xE, 'mnemonic': 'HAND',    'operation': 'Transmission / offering',           'family': 'coupling',       'barthel': 'Hand or arm extended'},
    '104': {'opcode': 0xF, 'mnemonic': 'EYE',     'operation': 'Perception / witnessing',           'family': 'coupling',       'barthel': 'Eye motif'},

    # ── PARITY (P) ── Symmetry / protection ──
    # Barthel 200-209: Figures with symmetrical attributes
    '200': {'opcode': 0x10, 'mnemonic': 'TWIN',   'operation': 'Doubling / mirror symmetry',       'family': 'parity',         'barthel': 'Double-headed or twin figure'},
    '201': {'opcode': 0x11, 'mnemonic': 'CROWN',  'operation': 'Elevation / sacred status',         'family': 'parity',         'barthel': 'Figure with headdress'},
    '202': {'opcode': 0x12, 'mnemonic': 'SHIELD', 'operation': 'Protection / boundary guard',       'family': 'parity',         'barthel': 'Figure holding object'},
    '203': {'opcode': 0x13, 'mnemonic': 'BALANCE','operation': 'Equilibrium / reciprocity',         'family': 'parity',         'barthel': 'Symmetrical compound'},

    # ── FIDELITY (F) ── Transmission / medium ──
    # Barthel 300-309: Birds as messengers
    '300': {'opcode': 0x14, 'mnemonic': 'FRGATE', 'operation': 'Divine messenger / Makemake bird',  'family': 'fidelity',       'barthel': 'Frigatebird'},
    '301': {'opcode': 0x15, 'mnemonic': 'TERN',   'operation': 'Soul carrier / spirit flight',      'family': 'fidelity',       'barthel': 'Tern or seabird'},
    '302': {'opcode': 0x16, 'mnemonic': 'CHANT',  'operation': 'Oral transmission / incantation',   'family': 'fidelity',       'barthel': 'Bird with open beak'},
    '303': {'opcode': 0x17, 'mnemonic': 'FEATHER','operation': 'Writing / inscription mark',        'family': 'fidelity',       'barthel': 'Feather or plume'},

    # ── KINETICS (K) ── Motion / process ──
    # Barthel 400-409: Marine life in motion
    '400': {'opcode': 0x18, 'mnemonic': 'FISH',   'operation': 'Movement / flow / current',         'family': 'kinetics',       'barthel': 'Fish'},
    '401': {'opcode': 0x19, 'mnemonic': 'TURTLE', 'operation': 'Endurance / slow passage',          'family': 'kinetics',       'barthel': 'Sea turtle'},
    '402': {'opcode': 0x1A, 'mnemonic': 'OCTOPUS','operation': 'Transformation / adaptability',      'family': 'kinetics',       'barthel': 'Octopus or squid'},
    '403': {'opcode': 0x1B, 'mnemonic': 'WAVE',   'operation': 'Cyclical return / rhythm',          'family': 'kinetics',       'barthel': 'Wave or water pattern'},

    # ── CARDINALITY (G) ── Scale / quantity ──
    # Barthel 500-509: Plants as counting/growth
    '500': {'opcode': 0x1C, 'mnemonic': 'SPROUT', 'operation': 'Emergence / generation',            'family': 'cardinality',    'barthel': 'Sprout or young plant'},
    '501': {'opcode': 0x1D, 'mnemonic': 'TREE',   'operation': 'Full growth / completion',          'family': 'cardinality',    'barthel': 'Tree or branch'},
    '502': {'opcode': 0x1E, 'mnemonic': 'FRUIT',  'operation': 'Product / offspring / result',      'family': 'cardinality',    'barthel': 'Fruit or seed pod'},
    '503': {'opcode': 0x1F, 'mnemonic': 'LEAF',   'operation': 'Unit / individual instance',        'family': 'cardinality',    'barthel': 'Leaf'},

    # ── COMPOSITION (Γ) ── Arrangement / syntax ──
    # Barthel 600-609: Implements for making/arranging
    '600': {'opcode': 0x20, 'mnemonic': 'STAFF',  'operation': 'Authority / lineage marker',        'family': 'composition',    'barthel': 'Staff or rod'},
    '601': {'opcode': 0x21, 'mnemonic': 'PADDLE', 'operation': 'Direction / steering',              'family': 'composition',    'barthel': 'Paddle or oar'},
    '602': {'opcode': 0x22, 'mnemonic': 'HOOK',   'operation': 'Capture / binding',                 'family': 'composition',    'barthel': 'Fish hook'},
    '603': {'opcode': 0x23, 'mnemonic': 'CORD',   'operation': 'Sequence / concatenation',          'family': 'composition',    'barthel': 'Cord or lashing'},

    # ── CRITICALITY (Φ) ── Threshold / transformation ──
    # Barthel 700-709: Compound threshold markers
    '700': {'opcode': 0x24, 'mnemonic': 'GATE',   'operation': 'Threshold / passage point',         'family': 'criticality',    'barthel': 'Doorway or gate compound'},
    '701': {'opcode': 0x25, 'mnemonic': 'ALTAR',  'operation': 'Sacrifice / offering point',        'family': 'criticality',    'barthel': 'Platform or altar'},
    '702': {'opcode': 0x26, 'mnemonic': 'MERGE',  'operation': 'Fusion / compound formation',       'family': 'criticality',    'barthel': 'Two glyphs joined'},
    '703': {'opcode': 0x27, 'mnemonic': 'RIFT',   'operation': 'Division / splitting apart',        'family': 'criticality',    'barthel': 'Glyph with cleft'},

    # ── CHIRALITY (H) ── Orientation / memory ──
    # Barthel 800-809: Directional and memory markers
    '800': {'opcode': 0x28, 'mnemonic': 'LEFT',   'operation': 'Sinister / past / ancestor',        'family': 'chirality',      'barthel': 'Left-facing variant'},
    '801': {'opcode': 0x29, 'mnemonic': 'RIGHT',  'operation': 'Dexter / future / descendant',      'family': 'chirality',      'barthel': 'Right-facing variant'},
    '802': {'opcode': 0x2A, 'mnemonic': 'UPWARD', 'operation': 'Ascent / skyward / divine',         'family': 'chirality',      'barthel': 'Upward-pointing glyph'},
    '803': {'opcode': 0x2B, 'mnemonic': 'DOWN',   'operation': 'Descent / earthward / chthonic',    'family': 'chirality',      'barthel': 'Downward-pointing glyph'},

    # ── STOICHIOMETRY (Σ) ── Counting / enumeration ──
    # Barthel 900-909: Numerical and listing marks
    '900': {'opcode': 0x2C, 'mnemonic': 'ONE',    'operation': 'Singular / unique instance',        'family': 'stoichiometry',  'barthel': 'Single stroke or unit'},
    '901': {'opcode': 0x2D, 'mnemonic': 'MANY',   'operation': 'Plural / multiple instances',       'family': 'stoichiometry',  'barthel': 'Multiple strokes or dots'},
    '902': {'opcode': 0x2E, 'mnemonic': 'ALL',    'operation': 'Totality / completion set',         'family': 'stoichiometry',  'barthel': 'Enclosing all glyphs'},
    '903': {'opcode': 0x2F, 'mnemonic': 'LIST',   'operation': 'Catalogue / enumeration sequence',  'family': 'stoichiometry',  'barthel': 'Vertical list marks'},

    # ── WINDING (Ω) ── Cycle / return / closure ──
    # Barthel special: cyclic and closure glyphs
    '950': {'opcode': 0x30, 'mnemonic': 'CYCLE',  'operation': 'Cycle / return to origin',          'family': 'winding',        'barthel': 'Circle or ring'},
    '951': {'opcode': 0x31, 'mnemonic': 'CRESC',  'operation': 'Crescent moon / lunar cycle',       'family': 'winding',        'barthel': 'Crescent shape'},
    '952': {'opcode': 0x32, 'mnemonic': 'OURO',   'operation': 'Self-devouring / eternal return',   'family': 'winding',        'barthel': 'Serpent swallowing tail'},
    '953': {'opcode': 0x33, 'mnemonic': 'END',    'operation': 'Termination / closure of text',     'family': 'winding',        'barthel': 'Terminal mark'},
}

# Reverse lookup: opcode → (barthel_id, mnemonic)
OPCODE_MAP: dict[int, tuple[str, str]] = {
    v['opcode']: (k, v['mnemonic']) for k, v in PRIMITIVES.items()
}

# The 12 structural families with their IG primitive correspondence
FAMILY_TO_PRIMITIVE = {
    'dimensionality': 'Ð',   # D
    'topology':       'Þ',   # T
    'coupling':       'Ř',   # R
    'parity':         'Φ',   # P
    'fidelity':       'ƒ',   # F
    'kinetics':       'Ç',   # K
    'cardinality':    'Γ',   # G
    'composition':    'ɢ',   # Gm
    'criticality':    'φ̂',   # Ph
    'chirality':      'Ħ',   # H
    'stoichiometry':  'Σ',   # S
    'winding':        'Ω',   # W
}

# Glyphs sorted by length for longest-match-first scanning
_SORTED_BARTHEL = sorted(PRIMITIVES.keys(), key=len, reverse=True)
