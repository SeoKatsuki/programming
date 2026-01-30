print('Простые числа')
print()

import math

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

for num in range (a, b + 1):
    if num < 2:
        continue

    prostoe_chislo = True

    for delitel in range (2, int(math.isqrt(num)) + 1):
        if num % delitel == 0:
            prostoe_chislo = False
            break

    if prostoe_chislo:
        print(num)