print('Обмен значений')
print()

import random

A = [random.randint(1, 100) for i in range(5)]      # Список случайных чисел
print('Список чисел: ', *A)
print()

min_A = A.index(min(A))     # Индекс минимального значения

A[0], A[min_A] = A[min_A], A[0]     # Меняем местами мин и первое значение

print('Измененная версия списка: ', *A)