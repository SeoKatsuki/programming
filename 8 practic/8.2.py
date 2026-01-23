print('Only even numbers')
print()

all_num = True    # Флаг, что все числа четные

for i in range(10):    # Выполняем цикл 10 раз
    num = int(input('Введите число: '))
    if num % 2 != 0:
       all_num = False    # Если есть нечетные числа, то меняем флаг

if all_num:    # Если флаг остался четным
    print('YES')
else:
    print('NO')