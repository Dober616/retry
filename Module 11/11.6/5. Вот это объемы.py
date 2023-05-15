import math

earth = 1.08321 * 10**12
radius = float(input('Радиус планеты: '))
v = (4 / 3) * math.pi * radius**3

if v > earth:
    print(f'Объем планеты больше объема Земли в {round(v / earth, 3)} раз')
elif earth > v:
    print(f'Объем Земли больше объема планеты в {round(earth / v, 3)} раз')
else:
    print('Объемы равны')