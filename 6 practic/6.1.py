print("Диагностика состояния здоровья")
print('=' * 30)


# Просим полльзователя ввести показателя
temperature = float(input('Введите Вашу температуру(В ℃): '))
pressure = int(input('Введите Ваше давление (верхнее): '))
pulse = int(input('Введите Ваш пульс (уд/мин): '))

# Задаем условия, по которым будем определять состояния
if (36 <= temperature <= 37) and (110 <= pressure <= 130) and (60 <= pulse <= 100):
    print('Нормальное состояние')
elif ((35 <= temperature <= 37) or (37 <= temperature <= 38)) and ((150 <= pressure < 110) or (130 < pressure <= 140)) and ((55 <= pulse < 60) or (100 < pulse <= 110)):
    print('Легкое недомогание')
elif ((35 < temperature < 36) or (37 > temperature > 38)) and ((105 < pressure) or (pressure > 38)) and ((55 < pulse) or (pulse > 110)):
    print('Требуется врач')
else:
    print('Состояние не удается определить. Рекомендуем обратиться к врачу')