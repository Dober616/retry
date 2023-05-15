import math

number = float(input('Введите вещественное число: '))
print(f'Округление в большую сторону: {math.ceil(number)}')
print(f'Округление в меньшую сторону: {math.floor(number)}')
print(f'Модуль числа {number}: {abs(number)}')
print(f'Корень числа {number}: {math.sqrt(number)}')
print(f'Число {number} в {number} степени: {number ** number}')
print(f'Натуральный логарифм числа {number}: {math.log(number)}')
print(f'Логарифм числа {number} по основанию 2: {math.log(number, 2)}')
print(f'Логарифм числа {number} по основанию 10: {math.log(number, 10)}')
print(f'Синус числа {number}: {math.sin(number)}')
print(f'Косинус числа {number}: {math.cos(number)}')
