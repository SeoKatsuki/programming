print('Шахматная доска')
print()

size = 8

for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print('W', end = ' ')
        else:
            print('B', end = ' ')
    print()