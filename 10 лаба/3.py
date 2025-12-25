max_num = 0
first_input = True

while True:
    n = int(input("Введите натуральное число (или 0 для выхода): "))
    if n == 0:
        break
    
    if first_input:
        max_num = n
        first_input = False
    elif n > max_num:
        max_num = n

if not first_input:
    print("Самое большое число:", max_num)