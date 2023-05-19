def swim_dot(x):
    count = 0
    if x <= 10:
        return 'Ошибка, число должно быть больше 10'
    else:
        while x > 10:
            x /= 10
            count += 1
        return f'{x}*10**{count}'


number = int(input('Введите число: '))

print(swim_dot(number))


