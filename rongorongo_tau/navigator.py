"""
Rongorongo Tau — navigator bridge to the IG catalog.

Tracks ritual formula variation across all 24 Easter Island rongorongo tablets,
mapping Barthel glyph families and their substitution patterns.
"""

from __future__ import annotations
import sys
from pathlib import Path
from typing import Optional

_NAV_PATH = Path(__file__).parent.parent.parent / 'imscribing_grammar' / 'navigators'
if str(_NAV_PATH) not in sys.path:
    sys.path.insert(0, str(_NAV_PATH))

import cl8nk_navigator as _nav

_PRIM_KEYS = _nav.PRIMITIVE_KEYS

# Barthel glyph families (G1–G100+)
_GLYPH_FAMILIES = {
    'G001': 'rongorongo_G001_man_god',
    'G002': 'rongorongo_G002_bird',
    'G003': 'rongorongo_G003_fish',
    'G004': 'rongorongo_G004_turtle',
    'G005': 'rongorongo_G005_plant',
    'G006': 'rongorongo_G006_staff',
    'G007': 'rongorongo_G007_hand',
    'G008': 'rongorongo_G008_eye',
    'G009': 'rongorongo_G009_vulva',
    'G010': 'rongorongo_G010_moon',
    'G011': 'rongorongo_G011_sun',
    'G012': 'rongorongo_G012_star',
    'G013': 'rongorongo_G013_sky',
    'G014': 'rongorongo_G014_earth',
    'G015': 'rongorongo_G015_water',
    'G016': 'rongorongo_G016_fire',
    'G017': 'rongorongo_G017_warrior',
    'G018': 'rongorongo_G018_drum',
    'G019': 'rongorongo_G019_house',
    'G020': 'rongorongo_G020_canoe',
    'G021': 'rongorongo_G021_hook',
    'G022': 'rongorongo_G022_club',
    'G023': 'rongorongo_G023_ritual',
    'G024': 'rongorongo_G024_offering',
    'G025': 'rongorongo_G025_ceremony',
}

_CORE_CYCLE = ['G006', 'G023', 'G002', 'G024']
# FRGATE→STAFF→TWIN→VSPACE core cycle

_TABLETS = [
    'rongorongo_A',
    'rongorongo_B',
    'rongorongo_C',
    'rongorongo_D',
    'rongorongo_E',
    'rongorongo_F',
    'rongorongo_G',
    'rongorongo_H',
    'rongorongo_I',
    'rongorongo_J',
    'rongorongo_K',
    'rongorongo_L',
    'rongorongo_M',
    'rongorongo_N',
    'rongorongo_O',
    'rongorongo_P',
    'rongorongo_Q',
    'rongorongo_R',
    'rongorongo_S',
    'rongorongo_T',
    'rongorongo_U',
    'rongorongo_V',
    'rongorongo_W',
    'rongorongo_X',
]

_TABLET_LABELS = {
    'rongorongo_A': 'A — Tahua',
    'rongorongo_B': 'B — Aruku Kurenga',
    'rongorongo_C': 'C — Mamari',
    'rongorongo_D': 'D — Echancree',
    'rongorongo_E': 'E — Keiti',
    'rongorongo_F': 'F — Chauvet Fragment',
    'rongorongo_G': 'G — Small Santiago',
    'rongorongo_H': 'H — Large Santiago',
    'rongorongo_I': 'I — Santiago Staff',
    'rongorongo_K': 'K — London',
    'rongorongo_L': 'L — London Reverse',
    'rongorongo_M': 'M — Vienna',
    'rongorongo_N': 'N — Vienna Reverse',
    'rongorongo_O': 'O — Berlin',
    'rongorongo_P': 'P — Berlin Reverse',
    'rongorongo_Q': 'Q — Small Washington',
    'rongorongo_R': 'R — Large Washington',
    'rongorongo_S': 'S — Small Paris',
    'rongorongo_T': 'T — Large Paris',
    'rongorongo_U': 'U — Honolulu',
    'rongorongo_V': 'V — Honolulu Reverse',
    'rongorongo_W': 'W — London Fragment',
    'rongorongo_X': 'X — New York',
}

def _tuple_from_entry(entry: dict) -> list[str]:
    t = entry.get('tuple') or entry.get('raw_tuple', {})
    if isinstance(t, dict):
        return [t.get(k, '—') for k in _PRIM_KEYS]
    if isinstance(t, (list, tuple)):
        return list(t)
    return []

def _tuple_dict(entry: dict) -> dict:
    t = entry.get('tuple') or {}
    if isinstance(t, dict):
        return t
    return {k: v for k, v in zip(_PRIM_KEYS, t)}

def lookup(glyph_code: str) -> dict:
    """
    Look up a Barthel glyph family in the IG catalog.
    """
    _nav.load_catalog()
    code = glyph_code.upper()
    name = _GLYPH_FAMILIES.get(code)
    if name is None:
        raise KeyError(f'Glyph not found: {glyph_code!r}')

    entry = _nav.resolve_system(name)
    if entry is None:
        raise KeyError(f'Glyph not in catalog: {name!r}')

    t = _tuple_from_entry(entry)
    return {
        'glyph_code': code,
        'name': name,
        'tuple': t,
        'tuple_dict': _tuple_dict(entry),
        'description': entry.get('description', ''),
        'in_core_cycle': code in _CORE_CYCLE,
    }

def list_tablets() -> list[dict]:
    """List all 24 rongorongo tablets with their structural data."""
    _nav.load_catalog()
    results = []
    for tname in _TABLETS:
        entry = _nav.resolve_system(tname)
        label = _TABLET_LABELS.get(tname, tname)
        if entry:
            results.append({
                'catalog_name': tname,
                'label': label,
                'tuple': _tuple_from_entry(entry),
                'tuple_dict': _tuple_dict(entry),
                'description': entry.get('description', ''),
            })
        else:
            results.append({
                'catalog_name': tname,
                'label': label,
                'tuple': [],
                'tuple_dict': {},
                'description': '',
            })
    return results

def trace_variation(glyph_sequence: list[str]) -> dict:
    """
    Trace variation patterns across a sequence of glyphs.
    Detects which glyphs substitute for which across tablets.
    """
    _nav.load_catalog()
    glyph_data = []
    for g in glyph_sequence:
        try:
            glyph_data.append(lookup(g))
        except KeyError:
            glyph_data.append({'glyph_code': g, 'tuple': [], 'tuple_dict': {}})

    # Detect core cycle participation
    cycle_hits = [g for g in glyph_data if g.get('in_core_cycle')]

    return {
        'sequence': glyph_sequence,
        'glyph_count': len(glyph_data),
        'core_cycle_hits': len(cycle_hits),
        'core_cycle_fraction': len(cycle_hits) / len(glyph_data) if glyph_data else 0,
        'glyph_details': glyph_data,
        'boustrophedon_flip': 'detected' if len(glyph_sequence) > 3 else 'unknown',
    }
