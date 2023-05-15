import math

distance = float(input('Расстояние до танка: '))
angle = float(input('Направление на танк: '))
x = distance * math.cos(angle)
y = distance * math.sin(angle)
print(f'Координаты танка: ({x}, {y})')