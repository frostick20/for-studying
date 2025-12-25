count_between = 0
found_alexandra = False

while True:
    name = input("Введите имя участника (или 'стоп' для завершения): ")
    
    if name.lower() == 'стоп':
        break

    if name == "Александра":
        found_alexandra = True
        continue 

    if name == "Левон":
        break 

    if found_alexandra:
        count_between += 1

print(f"Количество людей между ними: {count_between}")