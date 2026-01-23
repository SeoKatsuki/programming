print('Простой каллькулятор')
print('=' * 30)

num1, num2 = map(float, input('Введите два числа (через пробел): ').split())
action = input('Введите действие (+, -, *, /): ')

match action:
    case '+':
        print(round(num1 + num2, 2))
    case '-':
        print(round(num1 - num2, 2))
    case '*':
        print(round(num1 * num2,2))
    case '/':
        print(round(num1 / num2, 2))
    case _:
        print('ошибка ввода данных')
