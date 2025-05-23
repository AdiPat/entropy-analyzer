from typing import Any, Optional
from .entropy_strategy_base import EntropyStrategy
from .text_entropy import TextEntropy
from .numerical_entropy import NumericalEntropy
from .search_entropy import SearchEngineEntropy
from .contextual_entropy import ContextualEntropy
from .time_entropy import TimeEntropy


class EntropyFactory:
    """Factory class for creating entropy calculator instances.

    This factory manages the creation of different entropy calculation strategies,
    providing a centralized way to instantiate the appropriate calculator based
    on the type of data being analyzed.
    """

    @staticmethod
    def get_entropy_calculator(strategy_type: Optional[str]) -> EntropyStrategy:
        if not isinstance(strategy_type, str) or strategy_type is None:
            raise ValueError("Strategy type must be a string")

        strategies = {
            "text": TextEntropy(),
            "numerical": NumericalEntropy(),
            "search": SearchEngineEntropy(),
            "contextual": ContextualEntropy(),
            "time": TimeEntropy(),
        }

        if strategy_type not in strategies:
            raise ValueError(f"Invalid Strategy Type: {strategy_type}")

        return strategies[strategy_type]
