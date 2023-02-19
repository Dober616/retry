contribution = int(input('Введите сумму вклада: '))
percents = int(input('Введите годовой процент: '))
target = int(input('Желаемая сумма: '))
year = 0
while contribution < target:
    year += 1
    contribution += round(contribution * percents / 100, 2)
print(f'Итоговая полученная сумма: {round(contribution, 2)}')
print(f'Прошло {year} лет')
