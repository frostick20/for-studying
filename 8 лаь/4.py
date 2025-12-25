m = float(input("Стартовое количество организмов: "))
p = float(input("Среднесуточное увеличение в %: "))
n = int(input("Количество дней: "))

current_population = m
for day in range(1, n + 1):
    print(f"{day} {current_population}")
    current_population += current_population * (p / 100)