import math

for _ in range(3):
    number = float(input('Введите любое вещественное число: '))
    if number > 0:
        number = math.ceil(number)
        print(f'Число болmше нуля. Его логарифм: {math.log(number)}')
    else:
        number = math.floor(number)
        print(f'Число меньше нуля. Его экпанента: {math.exp(number)}')