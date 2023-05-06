hours = int(input('Сколько часов до конца эксперимента: '))
cells = 1
time = 0
for i in range(hours, 0, -3):
    cells *= 2
    time += 3
    print(f'Прошло {time} часов.\nКлеток: {cells}\nДо конца эксперимента {hours - time} часов')
    print()
