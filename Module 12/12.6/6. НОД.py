first_numm = int(input('Введите первое число: '))
secnd_numm = int(input('Введите второе число: '))


def nod(x, y):
    if x > y:
        number = x
        deliver = y
    elif x < y:
        number = y
        deliver = x
    else:
        return x

    for i in range(deliver, 1, -1):
        if number % i == 0 and deliver % i == 0:
            return i


print(f'Наибольший общий делитель: {nod(first_numm, secnd_numm)}')
