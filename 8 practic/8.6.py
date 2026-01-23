print('Угадай число за 3 попытки')
print()

from random import randint

number = randint(1, 10)   # Просим программу загадать число через рандомайзер
attempt = 3    # Вводим количество попыток

for i in range(1, attempt + 1):    # Цикл перебора количества попыток
    num_user = int(input('Введите число: '))
    if num_user == number:
        print('Вы угадали!')
        break   # Выходим из цикла, если юзер угадал
    else:
        attempt -= 1
        print(f'Не угадали! Осталось {attempt} попыток')

    if attempt == 0:
        print('Попытки закончились! Вы проиграли')
