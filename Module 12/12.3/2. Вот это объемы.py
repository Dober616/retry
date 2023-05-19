import math


def area(r):
    s = 4 * math.pi * r ** 2
    return s


def volume(r):
    v = ((4 / 3) * math.pi) * r ** 3
    return v

radius = int(input('Введите радиус планеты: '))
print(f'Площадь сферы: {area(radius)}\nОбъем шара: {volume(radius)}')