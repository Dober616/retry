x, y = float(input('Введите координаты X: ')), float(input('Введите координаты Y: '))
vertical = int(x * 10)
horizontal = int(y * 10)
if 0 < x < 0.8 or 0 < y < 0.8:
    print(f'Фигура находится в клетке ({vertical}, {horizontal})')
else:
    print('Клетки с такой координатой не существует')
