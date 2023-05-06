step = int(input('Введите шаг: '))
for i in range(4):
    sum = 0
    number = int(input(f'Введите первое число адреса {i + 1}-го ip: '))
    for _ in range(3):
        print(f'{number}', end='.')
        number += step
        sum += number
    print(sum)


