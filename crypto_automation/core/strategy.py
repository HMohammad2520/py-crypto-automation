from abc import abstractmethod
from typing import Literal

class Strategy:
    """Base class for all strategies"""
    from .bot import CryptoBot
    from .trader import Trader
    _bot: CryptoBot
    context: object
    trader: Trader

    @abstractmethod
    def get_signal(self) -> Literal['buy', 'sell', 'hold', 'error']:
        ...