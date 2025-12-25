NOMINALS = (5000, 2000, 1000, 500, 200, 100)

amount = int(input("Введите сумму для снятия (кратную 100): "))

if amount % 100 != 0:
    print("Ошибка: сумма должна быть кратна 100.")
else:
    print(f"Отчет о выдаче суммы {amount}:")
    temp_amount = amount
    for nominal in NOMINALS:
        count = temp_amount // nominal
        if count > 0:
            print(f"Купюры номиналом {nominal}: {count} шт.")
            temp_amount %= nominal