first_price = int(input('Цена 1-го стула: '))
secnd_price = int(input('Цена 2-го стула: '))
third_price = int(input('Цена 3-го стула: '))
percent = 10
summ = sum([first_price, secnd_price, third_price])
if summ > 10000:
    print(f'Итоговая стоимость стульев со скидкой {summ + summ * percent / 10}')
else:
    print(f'Итоговая стоимость стульев {summ}')