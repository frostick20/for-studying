import random

target = random.randint(1, 10)
guessed = False

for i in range(3):
    attempt = int(input(f"Попытка {i+1}. Введите число от 1 до 10: "))
    if attempt == target:
        print("Угадали!")
        guessed = True
        break
    elif attempt < target:
        print("Неверно (загаданное число больше)")
    else:
        print("Неверно (загаданное число меньше)")

if not guessed:
    print(f"Попытки закончились. Было загадано число {target}")