print('Наибольшие числа')
print()

number = int(input('Введите количество вводимых чисел: '))   # Сколько чисел выводим

max1 = 0
max2 = 0     # Оба максимальных числа пока равны 0

for i in range(number):     # Перебор чисел пользователя
    num_user = int(input('Введите число: '))
    if num_user > max1:
        max2 = max1    # Второе число по величине
        max1 = num
    elif num_user > max2:
        max2 = num_user    # Второе число по величине

print()
print(f'Первое максимальное число: {max1}\nВторое максимальное число: {max2}')








