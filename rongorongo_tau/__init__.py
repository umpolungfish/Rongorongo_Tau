from .navigator import lookup, list_tablets, trace_variation
from . import navigator

import sys
from pathlib import Path
_ENGINE = Path(__file__).parent.parent.parent / 'lang' / 'rongorongo-engine'
if str(_ENGINE) not in sys.path:
    sys.path.insert(0, str(_ENGINE))

from rongorongo_engine.session import RongorongoSession, SessionState

__version__ = '1.0.0'
__all__ = [
    'RongorongoSession',
    'SessionState',
    'lookup',
    'list_tablets',
    'trace_variation',
    'navigator',
]
