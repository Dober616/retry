import random
summ_money = 0
for i in range(12):
    money = random.randint(80000, 100000)
    print(f'Зарплата за {i + 1}-й месяц: {money}')
    summ_money += money
result = summ_money / 12
print(f'Средняя зарплата: {round(result, 2)}')
