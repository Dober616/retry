import random


def max_points(x):
    max_point = 0
    for point in x:
        if point > max_point:
            max_point = point
    return x.index(max_point)


def min_points(x):
    min_point = x[0]
    for point in x:
        if point < min_point:
            min_point = point
    return x.index(min_point)


n = int(input('Количество собак: '))
dogs_list = [random.randint(1, 20) for _ in range(n)]
print(dogs_list)
dogs_list[min_points(dogs_list)], dogs_list[max_points(dogs_list)] = dogs_list[max_points(dogs_list)], dogs_list[min_points(dogs_list)]
print(dogs_list)
