print("Популяция")
print()

m = int(input('Введите стартовое количество: '))
p = float(input('Введите процент прироста: '))
n = int(input('Введите количество дней: '))
print()

procente = m    # На первый день значение равно стартовому

for i in range(1, n + 1):    # Цикл перебора дней
    print(f'день {i}: {procente}')   # Принтуем текущий день
    procente = round(procente * (1 + p / 100), 2)