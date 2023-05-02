step = int(input('Введите шаг: '))
for i in range(4):
    print(f'\n{i + 1}-й IP', end=': ')
    for y in range(3):
        numm = int(input('Введите первое число IP: '))
        print(numm, end='.')
        numm += step
