print('Все вместе')
print()

user_num = int(input('Введите число'))

kol_troek = 0
last_num = user_num % 10
kol_chet = 0
sum_bolshe_pyati = 0
proiz_bolshe_semi = 0
kol_nol_or_pyati = 0

while user_num > 0:
    num = user_num % 10
    num == last_num

    if num == 3:
        kol_troek += 1

    if num == last_num:
        last_num += 1

    if num % 2 == 0:
        kol_chet += 1

    if num > 5:
        sum_bolshe_pyati += num

    if num > 7:
        proiz_bolshe_semi *= num

    if num == 0 or num == 5:
        kol_nol_or_pyati += 1