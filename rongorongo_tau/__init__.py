"""Corpus front-end package. The compilation engine is the installed
`rongorongo_engine` distribution; the session protocol is re-exported when that engine
ships one."""

from .navigator import lookup, list_tablets, trace_variation
from . import navigator

# The engine ships as an installed package; its seven-gate session is optional
# and only some corpora implement it. Re-export it when present.
try:
    from rongorongo_engine.session import RongorongoSession, SessionState  # noqa: F401
    _HAS_SESSION = True
except ImportError:
    _HAS_SESSION = False

__version__ = '1.0.0'

__all__ = ['lookup', 'list_tablets', 'trace_variation', 'navigator']
if _HAS_SESSION:
    __all__ += ['RongorongoSession', 'SessionState']
