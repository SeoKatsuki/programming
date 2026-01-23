print('Калькулятор тригонометрического выражения')

import math
x=float(input("Введите градусы:"))

# Переведем градусы в радианы
x=math.radians(x)

# Вычислим тригонометрическую функцию
u=math.sin(x) + math.cos(x) + math.tan(x) ** 2
print(u)
