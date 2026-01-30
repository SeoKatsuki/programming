print('Цифровой корень')
print()

num = int(input('Введите целое число: '))

while num >= 10:
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num //= 10
    num = sum_num

print(num)