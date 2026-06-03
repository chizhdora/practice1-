"""Основные расчёты экономического эффекта и эффективности."""
from typing import List, Union, Optional
from ..utils.validators import validate_numbers, validate_discount_rate, normalize_to_list
from loguru import logger


def calculate_cash_flows(
    benefits: Union[int, float, List[Union[int, float]]],
    costs: Union[int, float, List[Union[int, float]]],
    periods: int
) -> List[float]:
    """Рассчитывает денежные потоки CF = Выгоды - Затраты за каждый период."""
    logger.info("Расчёт денежных потоков")
    
    ben_list = normalize_to_list(benefits, periods, "выгоды")
    cost_list = normalize_to_list(costs, periods, "затраты")
    
    validate_numbers(ben_list, allow_negative=False, field_name="Выгоды")
    validate_numbers(cost_list, allow_negative=False, field_name="Затраты")
    
    cash_flows = [b - c for b, c in zip(ben_list, cost_list)]
    logger.success(f"Рассчитано {len(cash_flows)} периодов")
    return cash_flows


def calculate_total_effect(cash_flows: List[float]) -> float:
    """Рассчитывает общий экономический эффект (сумму всех потоков)."""
    validate_numbers(cash_flows, allow_negative=True, field_name="Денежные потоки")
    return sum(cash_flows)


def calculate_npv(
    cash_flows: List[float],
    discount_rate: float,
    initial_investment: float = 0
) -> float:
    """
    Рассчитывает чистую приведённую стоимость (NPV).
    
    NPV = -I₀ + Σ(CFₜ / (1 + r)ᵗ)
    """
    logger.info("Расчёт NPV")
    
    validate_numbers(cash_flows, allow_negative=True, field_name="Денежные потоки")
    validate_discount_rate(discount_rate)
    
    if initial_investment < 0:
        from ..exceptions import NegativeValueError
        raise NegativeValueError(f"Инвестиции не могут быть отрицательными: {initial_investment}")
    
    npv = -initial_investment
    for t, cf in enumerate(cash_flows, start=1):
        npv += cf / ((1 + discount_rate) ** t)
    
    logger.success(f"NPV = {npv:.2f}")
    return npv


def analyze_project(
    benefits: Union[int, float, List[Union[int, float]]],
    costs: Union[int, float, List[Union[int, float]]],
    discount_rate: float,
    initial_investment: float = 0,
    periods: Optional[int] = None,
    project_name: str = "Проект"
) -> dict:
    """Полный анализ инвестиционного проекта."""
    
    if periods is None:
        if isinstance(benefits, list):
            periods = len(benefits)
        elif isinstance(costs, list):
            periods = len(costs)
        else:
            raise ValueError("Укажите periods, если benefits и costs — числа")
    
    cash_flows = calculate_cash_flows(benefits, costs, periods)
    total_effect = calculate_total_effect(cash_flows)
    npv = calculate_npv(cash_flows, discount_rate, initial_investment)
    
    return {
        "project_name": project_name,
        "cash_flows": cash_flows,
        "total_effect": total_effect,
        "npv": npv,
        "is_profitable": npv > 0,
        "periods": periods,
        "initial_investment": initial_investment,
        "discount_rate": discount_rate
    }