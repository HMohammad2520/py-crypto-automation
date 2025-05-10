# crypto_automation\__init__.py
from .core.bot import CryptoBot
from .core.strategy import Strategy
from .core.trader import Trader
from .__version__ import __version__ as version

__all__ = [
    "CryptoBot",
    "Strategy",
    "Trader",
    "version",
]

from ._utils import logger
logger.debug('Imported py-crypto-automation')