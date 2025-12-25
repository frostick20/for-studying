n = int(input("Введите натуральное число n: "))
i = 1
while i <= n:
    if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
        i += 1
        continue
    print(i)
    i += 1

