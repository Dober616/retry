x = int(input('Введите количество мальчиков: '))
y = int(input('Введите количество девочек: '))
if x - y > 2 or y - x > 2:
    print('Решения нет')
elif x > y:
    for _ in range(y):
        print('BGB', end='')
elif x < y:
    for _ in range(x):
        print('GBG', end='')
elif x == y:
    for i in range(x):
        print('BG', end='')
