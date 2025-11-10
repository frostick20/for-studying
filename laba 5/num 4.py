import math

def calculate_rectangle_area(width, height):
    """
    Вычисляет площадь прямоугольника.
    width: ширина
    height: высота
    return: площадь
    """
    return width * height


def calculate_circle_area(radius):
    """
    Вычисляет площадь круга.
    radius: радиус круга
    return: площадь круга
    """
    return math.pi * (radius ** 2)


def task_4():
    w, h = map(float, input("Введите ширину и высоту прямоугольника: ").split())
    rect_area = calculate_rectangle_area(w, h)
    print(f"Площадь прямоугольника: {rect_area:.2f}")

    r = float(input("Введите радиус круга: "))
    circle_area = calculate_circle_area(r)
    print(f"Площадь круга: {circle_area:.2f}")
