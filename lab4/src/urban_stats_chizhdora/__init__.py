def calculate_npv(cash_flows: list, discount_rate: float = 0.1) -> float:
    """Чистая приведённая стоимость (NPV)."""
    npv = 0.0
    for t, cf in enumerate(cash_flows):
        npv += cf / ((1 + discount_rate) ** t)
    return round(npv, 2)


def calculate_cash_flow(benefits: float, costs: float) -> float:
    """Денежный поток = выгоды - затраты."""
    return round(benefits - costs, 2)


def calculate_total_effect(cash_flows: list) -> float:
    """Общий экономический эффект (сумма потоков)."""
    return round(sum(cash_flows), 2)


__all__ = ["calculate_npv", "calculate_cash_flow", "calculate_total_effect"]