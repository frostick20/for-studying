def chess_cell_color():
    try:
        x1, y1, x2, y2 = [int(input()) for _ in range(4)]
        
        if (x1 + y1) % 2 == (x2 + y2) % 2:
            print("YES")
        else:
            print("NO")
    except ValueError:
        print("Ошибка ввода")

chess_cell_color()