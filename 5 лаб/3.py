USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """
    Конвертирует сумму из долларов в рубли по заданному курсу.
    :param amount_usd: Сумма в долларах (float)
    :return: Сумма в рублях (float)
    """
    return amount_usd * USD_TO_RUB

amount = float(input("Введите сумму в долларах: "))
result = convert_usd_to_rub(amount)

print(f"Сумма в рублях: {result:,.2f} руб.".replace(',', ' '))