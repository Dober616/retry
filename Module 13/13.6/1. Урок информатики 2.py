def swim_dot(x):
    count = 0
    if x <= 0:
        return 'Ошибка, число должно быть больше 10'
    elif x > 10:
        while x > 10:
            x /= 10
            count += 1
        return f'{x}*10**{count}'
    elif x < 1:
        while x < 1:
            x *= 10
            count += 1
        return f'{round(x)}*10**-{count}'
    else:
        return x


number = float(input('Введите число: '))

print(swim_dot(number))


