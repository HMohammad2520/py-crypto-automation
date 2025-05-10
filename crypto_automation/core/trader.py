from abc import abstractmethod
from crpto_automation.type_hints import SignalTypes

class Trader:
    """Base class for all traders"""
    from .bot import CryptoBot
    from .strategy import Strategy
    _bot: CryptoBot
    context: object
    strategy: Strategy

    def execute_signal(self, signal: SignalTypes) -> None:
        """Initialize a signal with the given type and name"""
        if signal == 'buy': self.buy()
        elif signal == 'sell': self.sell()
        elif signal == 'hold': self.hold()
        elif signal == 'error': self.error()
        else: raise ValueError(f"Invalid signal type: {signal}")

    @abstractmethod
    def buy(self) -> None:
        ...

    @abstractmethod
    def sell(self) -> None:
        ...

    @abstractmethod
    def hold(self) -> None:
        ...

    @abstractmethod
    def error(self) -> None:
        ...