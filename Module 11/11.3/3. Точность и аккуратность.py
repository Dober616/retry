x, y = 0.731, 0.167  # float(input('Введите координаты X: ')), float(input('Введите координаты Y: '))
horizontal = int(x * 10)
vertical = int(y * 10)
if 0 < x < 0.8 or 0 < y < 0.8:
    print(f'Фигура находится в клетке ({horizontal}, {vertical})')
else:
    print('Клетки с такой координатой не существует')
correct_x =  round(horizontal / 10 + 0.05 - x, 3)
correct_y = round(vertical / 10 + 0.05 - y, 3)
if correct_x > 0:
    print(f'Фигуру нужно сдвинуть на {abs(correct_x)} вправо', end='')
else:
    print(f'Фигуру нужно сдвинуть на {abs(correct_x)} влево')
if correct_y > 0:
    print(f' и на {abs(correct_y)} вниз')
else:
    print(f' и на {abs(correct_y)} вверх')
