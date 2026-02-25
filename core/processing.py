def process_data(data: str) -> str:
    """Функция возвращает строку в верхнем регистре."""
    return data.upper()

# Для тестирования модуля
if __name__ == "__main__":
    test_data = "hello"
    result = process_data(test_data)
    print(f"Тест: {test_data} -> {result}")