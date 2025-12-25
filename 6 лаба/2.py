def roulette_color():
    try:
        n = int(input("Введите номер кармана (0-36): "))
        
        if not (0 <= n <= 36):
            print("ошибка ввода")
        elif n == 0:
            print("зеленый")
        elif (1 <= n <= 10) or (19 <= n <= 28):
            print("красный" if n % 2 != 0 else "черный")
        elif (11 <= n <= 18) or (29 <= n <= 36):
            print("черный" if n % 2 != 0 else "красный")
            
    except ValueError:
        print("ошибка ввода")

roulette_color()