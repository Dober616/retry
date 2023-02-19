start = int(input('Введите начало отрезка: '))
finish = int(input('Введите конец отрезка: '))
for x in range(finish, start - 1, -1):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print(f'В точке {x} функция равна {y}')
