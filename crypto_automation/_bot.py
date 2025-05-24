# crypto_automation\core\bot.py
from typing import Any

from ._strategy import Strategy
from ._trader import Trader
from ._context import Context

class CryptoBot:
    """
    cryptocurrency trading bot.
    """
    def __init__(
            self,
            strategy: Strategy,
            trader: Trader,
            **context: Any,
            ) -> None:
        """
        Initialize the bot.

        Args:
            strategy (Strategy): The strategy to use for trading.
            trader (Trader): The trader to use for trading.
            **context (Any): Additional context to pass to the strategy and trader.
        """
        self.strategy = strategy
        self.trader = trader
        self._context_dict = context

        # Initiating context
        self.context = Context()
        [setattr(self.context, k, v) for k, v in context.items()]
        self.strategy.context = self.context
        self.trader.context = self.context

        # Connect strategy and trader
        self.strategy.trader = self.trader
        self.trader.strategy = self.strategy

    def run(self) -> None:
        """
        Run the bot once.
        """
        self.trader.execute_signal(self.strategy.get_signal())
