print('Банкомат')
print('=' * 35)

money = int(input('Введите сумму (руб.): '))

if money % 100 == 0:
    def bankomat_rub(amound_money):
        if money >= 5000:
            kol_5000 = money // 5000
            print(f'количество купюр по 5000 руб. - {kol_5000}')
            oststok = money - 5000 * kol_5000
        if money >= 2000:
            kol_2000 = money // 2000
            print(f'количество купюр по 2000 руб. - {kol_2000}')
            oststok = money - (2000 * kol_2000)
        if money >= 1000:
            kol_1000 = money // 1000
            print(f'количество купюр по 1000 руб. - {kol_1000}')
            oststok = money - (1000 * kol_1000)
        if money >= 500:
            kol_500 = money // 500
            print(f'количество купюр по 500 руб. - {kol_500}')
            oststok = money - (500 * kol_500)
        if money >= 200:
            kol_200 = money // 200
            print(f'количество купюр по 200 руб. - {kol_200}')
            oststok = money - (200 * kol_200)
        if money >= 100:
            kol_100 = money // 100
            print(f'количество купюр по 100 руб. - {kol_100}')
            oststok = money - (100 * kol_100)
    kupuri = bankomat_rub(money)
else:
    print("Сумма должна быть кратна 100 руб.")