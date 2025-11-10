TAX_RATE = 0.13  # налоговая ставка

def task_1():
    """Калькулятор подоходного налога."""
    income = float(input("Введите годовой доход: "))
    tax_amount = income * TAX_RATE
    net_income = income - tax_amount

    print(f"Общий доход: {income:,.2f} руб.")
    print(f"Налог: {tax_amount:,.2f} руб.")
    print(f"Доход после налога: {net_income:,.2f} руб.")
