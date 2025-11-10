DENOMINATIONS = [5000, 2000, 1000, 500, 200, 100]

def task_5():
    amount = int(input("Введите сумму для снятия (кратную 100): "))

    if amount % 100 != 0:
        print("Сумма должна быть кратной 100!")
        return

    print("\nВыдача купюр:")

    for bill in DENOMINATIONS:
        count = amount // bill
        amount %= bill
        print(f"{bill} руб.: {count} шт.")
