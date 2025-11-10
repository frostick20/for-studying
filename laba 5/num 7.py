def calculate_sum(a, b):
    """
    Возвращает сумму двух чисел.
    """
    return a + b


def task_7():
    """Улучшенный вариант программы стажера."""
    a, b = map(float, input("Введите два числа через пробел: ").split())
    result = calculate_sum(a, b)
    print(f"Сумма: {result}")
