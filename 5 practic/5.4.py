print('Универсальный калькулятор площади')
print('=' * 35)

def calculate_rectangle_area(widht, height):
    """
    Arguments:
         widht: ширина прямоугольника
         height: высота прямоугольника

    Returns:
        Площадь прямоугольника
    """
    return width * height

import math
def calculate_circle_area(radius):
    """
    Arguments:
        radius: радиус окружности

    Returns:
        Площадь окружности
    """
    return 2 * math.pi * radius

# Пользователь вводит размеры фигуры
width, height = map(float, input('Введите размеры прямоугольника (ширина и высота): ').split())
# Вычисляем площадь, вызывая def, и форматируем до двух знаков после запятой
S_tag = round(calculate_rectangle_area(width, height), 2)

radius = float(input ('Введите радиус круга: '))
S_cir = round(calculate_circle_area(radius), 2)

print('=' * 35)
print(f'Площадь прямоугольника составляет {S_tag}')
print(f'Площадь круга составляет {S_cir}')