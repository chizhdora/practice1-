"""Библиотека для экономических расчётов."""

from .core.calculators import (
    calculate_cash_flows,
    calculate_total_effect,
    calculate_npv,
    analyze_project
)

from .exceptions import (
    EconomicEffectError,
    InvalidInputError,
    NegativeValueError,
    PeriodMismatchError
)

__all__ = [
    "calculate_cash_flows",
    "calculate_total_effect",
    "calculate_npv",
    "analyze_project",
    "EconomicEffectError",
    "InvalidInputError",
    "NegativeValueError",
    "PeriodMismatchError",
]

__version__ = "1.0.0"