print('Конвертер валют')

# вводим функцию def
def convert_usd_to_rub(amound_usd):
    """
    Конвертируем из доллары в рубли

    Arguments:
        amound_usd: сумма в долларах для конвертации

    return:
        Сумма в рублях
    """
    usd_to_rub = 95.50
    return amound_usd * usd_to_rub

# Просим пользователя ввести доллары
usd = float(input('Введите сумму (в $): '))

# Переводим в рубли, используя def
rub = convert_usd_to_rud(usd)

print(f'Ваша сумма в рублях составляет {rub} руб.')