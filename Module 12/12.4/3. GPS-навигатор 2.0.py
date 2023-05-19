import math


def distance(a, b, c, d):
    result = (c - a) ** 2 + (d - b) ** 2
    return abs(math.sqrt(result))


question = int(input('Что ищем? (расстояние до точки: 0 / расстояние между точками: 1) : '))
if question == 0:
    x_1, y_1 = 0, 0
    x_2, y_2 = int(input('Введите координату X 2 точки: ')), int(input('Введите координату Y 2 точки: '))
    print(distance(x_1, y_1, x_2, y_2))
elif question == 1:
    x_1, y_1 = int(input('Введите координату X 1 точки: ')), int(input('Введите координату Y 1 точки: '))
    x_2, y_2 = int(input('Введите координату X 2 точки: ')), int(input('Введите координату Y 2 точки: '))
    print(distance(x_1, y_1, x_2, y_2))
else:
    print('Ошибка ввода...')

