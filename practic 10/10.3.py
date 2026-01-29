print('Рекордсмен')
print()

num = int(input('Введите число: '))

# Проверка числа под условие
if num == 0:
    print('Ошибка❌ Нельзя начинать с нуля')
else:
    max_num = num   # текущий максимум

    # цикл для последующих чисел
    while True:
        num = int(input('Введите число: '))
        if num == 0:
            break  # Выход из цикла, тк 0 сигнал окончания
        if num > max_num:
            max_num = num  # Обновляем максимум

    print(f'Максималное число: {max_num}')