weight, height = map(float, input("Введите вес (кг) и рост (м) через пробел: ").split())

bmi = weight / (height * height)

print(f"Ваш Индекс Массы Тела (ИМТ): {bmi:.1f}")