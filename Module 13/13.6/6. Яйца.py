def temp(x):
    d = x ** 3 - 3 * x ** 2 - 12 * x + 10
    return d


def turtle_eggs(max, min, z):
    while True:
        mid = (max + min) / 2
        if temp(mid) > z:
            min = mid
        elif temp(mid) < 0:
            max = mid
        else:
            return mid


max_dangerous = 0.1 #float(input('Введите максимально допустимый уровень опасности: '))
max_depth = 4
min_depth = 0
print(f'Оптимальная глубина: {turtle_eggs(max_depth, min_depth, max_dangerous)} м.')
