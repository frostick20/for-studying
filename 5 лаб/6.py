import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2 
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Введите координаты вершин треугольника:")
ax, ay = map(float, input("Точка A (x y): ").split())
bx, by = map(float, input("Точка B (x y): ").split())
cx, cy = map(float, input("Точка C (x y): ").split())

side_ab = calculate_distance(ax, ay, bx, by)
side_bc = calculate_distance(bx, by, cx, cy)
side_ca = calculate_distance(cx, cy, ax, ay)

area = calculate_triangle_area(side_ab, side_bc, side_ca)
print(f"Площадь треугольника: {area:.2f}")