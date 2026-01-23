print('Произведение чисел')
print()

proiz = 1

while True:
    num = int(input('Введите число: '))
    if num > 0:
        proiz *= num
    else:
        break

print(f'Результат произведения равен {proiz}')