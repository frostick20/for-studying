def task_2():
    """Калькулятор Индекса Массы Тела."""
    weight, height = map(float, input("Введите вес и рост (м) через пробел: ").split())
    bmi = weight / (height * height)
    print(f"Ваш ИМТ: {bmi:.1f}")
