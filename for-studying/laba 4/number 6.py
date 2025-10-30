import math

x = float(input("значение х:"))
rad = math.radians(x)
a = math.sin(rad) + math.cos(rad) + math.tan(rad) ** 2
print(a)