print('Пароль')
print()

password_true = 'admin'
attempts = 3

while True:
    password = input('Введите пароль: ')
    if password_true == password:
        print('Пароль верный. Загрузка экрана')
        break
    else:
        attempts -= 1
        print(f'Пароль неверный. Осталось попыток: {attempts}')

    if attempts == 0:
        print('Доступ заблокирован')
        break