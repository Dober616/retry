import random

money = 5000  #int(input('Введите количество денег: '))

while money < 10000:
    qube = random.randint(1, 6)
    if qube != 3:
        money += 500
        print(f'Выпало число {qube}\nВы выиграли 500 рублей, у вас осталось {money} рублей')
    else:
        money = 0
        print(f'Выпало число {qube}\nВы проиграли все. На счету {money} рублей')
        break
print(f'Игра закончена, на счету {money} рублей')