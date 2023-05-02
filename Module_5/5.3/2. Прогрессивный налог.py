import random

profit = random.randint(5000, 100000)
if profit < 1000:
    percent = 13

elif 10000 < profit < 50000:
    percent = 20
else:
    percent = 30
tax = profit * percent / 100
print(f'Прибыль: {profit}\nПроцентная ставка: {percent}\nНалог с прибыли: {tax}')
