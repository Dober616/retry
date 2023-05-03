money_summ = 0
while money_summ < 500000:
    money = int(input('Сколько денег отложить: '))
    money_summ += money
print(f'Поздравляем, вы накопили {money_summ}!')