num = int(input("Введите натуральное число: "))
original_num = num
last_digit = num % 10

count_3 = 0
count_last_digit = 0
count_even = 0
sum_greater_5 = 0
prod_greater_7 = 1
has_greater_7 = False
count_0_5 = 0

while num > 0:
    digit = num % 10

    if digit == 3: 
        count_3 += 1

    if digit == last_digit: 
        count_last_digit += 1

    if digit % 2 == 0: 
        count_even += 1

    if digit > 5: 
        sum_greater_5 += digit

    if digit > 7:
        prod_greater_7 *= digit
        has_greater_7 = True

    if digit == 0 or digit == 5: 
        count_0_5 += 1

    num //= 10

if not has_greater_7: 
    prod_greater_7 = 1 

print(count_3)
print(count_last_digit)
print(count_even)
print(sum_greater_5)
print(prod_greater_7)
print(count_0_5)