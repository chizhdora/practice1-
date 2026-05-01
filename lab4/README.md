# urban_stats_chizhdora

Библиотека для экономических расчётов городских проектов.

## Установка

```bash
pip install urban-stats-chizhdora

## Быстрый старт
from urban-stats-chizhdora import calculate_npv, calculate_cash_flow, calculate_total_effect

# Денежный поток за год
cf = calculate_cash_flow(100, 80)
print(f"Денежный поток: {cf}")

# NPV для 3 лет
npv = calculate_npv([20, 20, 20], 0.1)
print(f"NPV: {npv}")

# Общий эффект
total = calculate_total_effect([20, 30, 50])
print(f"Общий эффект: {total}")

Лабораторная работа №4 выполнена 
    