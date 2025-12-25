def bishop_move():
    try:
        x1, y1, x2, y2 = [int(input()) for _ in range(4)]
        
        if abs(x1 - x2) == abs(y1 - y2):
            print("YES")
        else:
            print("NO")
    except ValueError:
        print("Ошибка ввода")

bishop_move()