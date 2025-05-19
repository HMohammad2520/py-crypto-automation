# crypto_automation\__init__.py
from ._bot import CryptoBot
from ._strategy import Strategy
from ._trader import Trader
from .__version__ import __version__ as version

__all__ = [
    "CryptoBot",
    "Strategy",
    "Trader",
    "version",
]