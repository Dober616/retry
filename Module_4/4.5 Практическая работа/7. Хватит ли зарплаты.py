work_hours = int(input('Количество отработанных часов: '))
food_money = int(input('Деньги на еду: '))
credit = int(input('Ежемесячный платежь по кредиту: '))
result = (200 * work_hours) / 2 ** 3 + work_hours
if food_money + credit < result:
    print('Денег не хватит, ищи другую работу')
else:
    print('Нормальная работа, денег хватает')