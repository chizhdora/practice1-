"""Валидация входных данных."""
from typing import List, Union
from ..exceptions import InvalidInputError, NegativeValueError, PeriodMismatchError


def validate_numbers(values: List[Union[int, float]], 
                    allow_negative: bool = False,
                    field_name: str = "значение") -> None:
    """Проверяет, что все элементы списка являются числами."""
    for i, val in enumerate(values):
        if not isinstance(val, (int, float)):
            raise InvalidInputError(
                f"{field_name} на позиции {i} имеет тип {type(val).__name__}, ожидалось число"
            )
        if not allow_negative and val < 0:
            raise NegativeValueError(
                f"{field_name} на позиции {i} отрицательное: {val}"
            )


def validate_discount_rate(rate: Union[int, float]) -> None:
    """Проверяет ставку дисконтирования."""
    if not isinstance(rate, (int, float)):
        raise InvalidInputError(f"Ставка должна быть числом, получен {type(rate).__name__}")
    if rate < 0:
        raise NegativeValueError(f"Ставка не может быть отрицательной: {rate}")


def normalize_to_list(values: Union[int, float, List[Union[int, float]]], 
                     periods: int,
                     field_name: str = "значение") -> List[float]:
    """Приводит входные данные к списку нужной длины."""
    from ..exceptions import InvalidInputError, PeriodMismatchError
    
    # Случай 1: число
    if isinstance(values, (int, float)):
        return [float(values)] * periods
    
    # Случай 2: список
    if isinstance(values, list):
        # Проверяем каждый элемент списка
        for i, v in enumerate(values):
            if not isinstance(v, (int, float)):
                raise InvalidInputError(
                    f"Элемент {i} в списке {field_name} должен быть числом, "
                    f"получен {type(v).__name__}"
                )
        
        if len(values) != periods:
            raise PeriodMismatchError(
                f"Длина списка {field_name} ({len(values)}) != {periods}"
            )
        return [float(v) for v in values]
    
    # Случай 3: что-то другое
    raise InvalidInputError(
        f"{field_name} должно быть числом или списком, "
        f"получен {type(values).__name__}"
    )
