import time
from abc import abstractmethod
from typing import Any

from .strategy import Strategy
from .trader import Trader

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
        self.context = object()
        [setattr(self.context, k, v) for k, v in context.items()]
        self.strategy.context = self.context
        self.trader.context = self.context

        # Connect strategy and trader
        self.strategy.trader = self.trader
        self.trader.strategy = self.strategy
    
        self._running = None

    def run(self, each_iter: float) -> None:
        """
        Run the bot in a loop.

        Args:
            each_iter (float): The time interval between each iteration in seconds.
        """
        self._running = True
        while self._running:
            self.trader.execute_signal(self.strategy.get_signal())
            time.sleep(each_iter)
    
    def stop(self) -> None:
        """
        Stop the bot.
        """
        self._running = False
