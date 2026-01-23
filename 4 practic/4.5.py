print("Временной интервал")

import math
Min=int(input("Введите минуты:"))

# Переведем в часы
hour=math.floor(Min / 60)

# Узнаем какое количество осталось минут, не переведенных в часы
minute=math.floor(Min % 60)
print(Min, "мин - это", hour, "час", minute, "минут")