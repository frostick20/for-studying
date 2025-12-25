def queen_move():
    try:
        x1, y1, x2, y2 = [int(input()) for _ in range(4)]

        is_rook_move = (x1 == x2 or y1 == y2)
        is_bishop_move = abs(x1 - x2) == abs(y1 - y2)
        
        if is_rook_move or is_bishop_move:
            print("YES")
        else:
            print("NO")
    except ValueError:
        print("Ошибка ввода")

queen_move()