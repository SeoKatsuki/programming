print('Калькулятор поездки на такси')
print('=' * 35)

def calculate():
    price = 49.5
    distance = float(input('Введите расстояние (км): '))
    liter = float(input('Введите сколько литров бензина потребуется на 100 км: '))
    total_l = distance * (1 / 100)
    total_p = price * total_l
    return total_p, total_l

total_p, total_l = calculate()
total_l = round(total_l, 2)
total_p = round(total_p, 2)

print("=" * 35)
print(f'Потребуется бензина для Вашей поездки: {total_l} л.')
print(f'Стоимость составляет: {total_p} руб.')
