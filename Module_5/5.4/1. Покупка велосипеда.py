import random

gears = random.randint(18, 30)
year = random.randint(2015, 2021)
print(f'{gears} скоростей')
print(f'Год выпуска: {year}')
if gears >= 24 and year >= 2018:
    print('Велик нам подходит')
else:
    if gears < 24:
        print('Скоростей маловато')
    elif gears < 2018:
        print('Староват велик')