"""Пользовательские исключения библиотеки economic_effect."""

class EconomicEffectError(Exception):
    """Базовое исключение для всех ошибок библиотеки."""
    pass

class InvalidInputError(EconomicEffectError):
    """Исключение при неверном типе входных данных."""
    pass

class NegativeValueError(EconomicEffectError):
    """Исключение при отрицательных значениях, где они недопустимы."""
    pass

class PeriodMismatchError(EconomicEffectError):
    """Исключение при несоответствии количества периодов."""
    pass