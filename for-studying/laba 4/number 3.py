a = str(input())
score = 0

for i in a:
    score = score + 1
    if score == 1:
        print("Цифра в позиции тысяч равна:" + " " + i)
    elif score == 2:
        print("Цифра в позиции сотен равна:" + " " + i)
    elif score == 3:
        print("Цифра в позиции десятков равна:" + " " + i)
    else:
        print("Цифра в позиции единиц равна:" + " " + i)