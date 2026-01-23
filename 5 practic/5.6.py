print('Калькулятор площади треугольника')
print('=' * 35)

def calculate_distance(x1, y1, x2, y2 ):
    return x1 - y1, x2 - y2

import math
def calculate_triangle_area(a, b, c):
    p = a + b + c
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = map(float, input('Введите координаты вершины А (x, y): ').split())
x2, y2 = map(float, input('Введите координаты вершины B (x, y): ').split())
x3, y3 = map(float, input('Введите координаты вершины C (x, y): ').split())

dis_AB = calculate_distance(x1, y1, x2, y2)
dis_BC = calculate_distance(x2, y2, x3, y3)
dis_AC = calculate_distance(x3, y3, x1, y1)

S = round(calculate_triangle_area(dis_AB, dis_BC, dis_AC), 2)
print(f'Площадь треугольника равняется {S}')
