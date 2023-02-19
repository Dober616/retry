name = input('Имя должника: ')
money = int(input('Сумма долга: '))
summ = 0
while summ < money:
    pay = int(input(f'{name}, какую сумму вы готовы внести? '))
    summ += pay
    if summ < money:
        print('Денег пока недостаточно...')
    else:
        pass
print(f'Поздравляем, {name}, вы погасили долг!')
