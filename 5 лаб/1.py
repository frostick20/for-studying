TAX_RATE = 0.13

income = float(input("Введите ваш годовой доход: "))

tax_amount = income * TAX_RATE
income_after_tax = income - tax_amount

print(f"Общая сумма дохода: {income:,.2f} руб.".replace(',', ' '))
print(f"Сумма рассчитанного налога: {tax_amount:,.2f} руб.".replace(',', ' '))
print(f"Сумма «на руки» после вычета налога: {income_after_tax:,.2f} руб.".replace(',', ' '))