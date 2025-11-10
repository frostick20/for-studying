USD_TO_RUB = 95.50  # курс доллара

def convert_usd_to_rub(amount_usd):
    """
    Конвертирует сумму в долларах в рубли.
    amount_usd: сумма в USD
    return: сумма в RUB
    """
    return amount_usd * USD_TO_RUB


def task_3():
    amount = float(input("Введите сумму в долларах: "))
    result = convert_usd_to_rub(amount)
    print(f"{amount:.2f} USD = {result:,.2f} RUB")
