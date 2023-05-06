education_grant = int(input('Введите размер стипендии: '))
living_expences = int(input('Введите расходы на проживание: '))
for month in range(12):
    print(f'Месяц {month + 1} - траты: {round(living_expences, 2)}. Не хватает {round(living_expences - education_grant, 2)}')
    living_expences += living_expences * 3 / 100
