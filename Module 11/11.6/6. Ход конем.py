import math

starting_pos_x = float(input('Позиция коня по горизонтали: '))
starting_pos_y = float(input('Позиция коня по вертикали: '))
cell_x = math.floor(starting_pos_x * 10)
cell_y = math.floor(starting_pos_y * 10)
if 0 < cell_x < 8 or 0 < cell_y < 8:
    print(f'Конь находится в клетке {cell_x}, {cell_y}')
else:
    print('Конь не может находиться за пределами доски! Попробуйте еще раз...')

finish_pos_x = float(input('Позиция коня по горизонтали: '))
finish_pos_y = float(input('Позиция коня по вертикали: '))
point_x = math.floor(finish_pos_x * 10)
point_y = math.floor(finish_pos_y * 10)
if 0 < finish_pos_x < 8 or 0 < finish_pos_y < 8:
    print(f'Точка в клетке {cell_x}, {cell_y}')
else:
    print('Конь не может находиться за пределами доски! Попробуйте еще раз...')

if abs(cell_x - point_x) == 1 and abs(cell_y - point_y) == 2 or abs(cell_x - point_x) == 2 and abs(cell_y - point_y) == 1:
    print('Отлично, ход засчитан')
else:
    print('Конь так не ходит')