def maximum_of_two(x, y):
    if x > y:
        # print('Наибольшее число: \n')
        return x
    elif x < y:
        # print('Наибольшее число: \n')
        return y
    else:
        # print('Числа равны')
        return x


def maximum_of_three(x, y, z):
    if maximum_of_two(x, y) > z:
        return f'Наибольшее число: {maximum_of_two(x, y)}'
    elif maximum_of_two(x, y) < z:
        return f'Наибольшее число: {z}'
    else:
        return 'Все числа равны'


number_count = int(input('Сколько чисел сравниваем: '))
numm_list = [int(input('Введите число: ')) for _ in range(number_count)]

if number_count == 2:
    print(maximum_of_two(numm_list[0], numm_list[1]))
elif number_count == 3:
    print(maximum_of_three(numm_list[0], numm_list[1], numm_list[2]))
