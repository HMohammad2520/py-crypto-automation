# crypto_automation\core\strategy.py
from abc import abstractmethod
from typing import Literal

class Strategy:
    """Base class for all strategies"""
    from ._bot import CryptoBot
    from ._trader import Trader
    _bot: CryptoBot
    context: object
    trader: Trader

    @abstractmethod
    def get_signal(self) -> Literal['buy', 'sell', 'hold', 'error']:
        ...