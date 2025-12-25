total_sum = 0

while True:
    price = int(input("Введите цену товара (или 0 для завершения): "))
    if price == 0:
        break
    if price < 0:
        print("Ошибка цены")
        continue
    
    total_sum = total_sum + price

if total_sum > 1000:
    discount = total_sum * 0.10
    total_sum = total_sum - discount
    print("Сумма со скидкой 10%:", total_sum)
else:
    print("Итоговая сумма:", total_sum)