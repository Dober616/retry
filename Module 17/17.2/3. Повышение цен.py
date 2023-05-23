count = int(input('Количество товаров: '))
prices = list()
for _ in range(count):
    price = float(input('Введите цену на товар: '))
    prices.append(price)

price_increase_first = 8
price_increase_secnd = 12

first_year_prices = [i + i * price_increase_first / 100 for i in prices]
secnd_year_prices = [i + i * price_increase_secnd / 100 for i in prices]

print(f'Сумма начальных цен {round(sum(prices), 2)}')
print(f'Сумма цен в первый год {round(sum(first_year_prices), 2)}')
print(f'Сумма цен во второй год {round(sum(secnd_year_prices), 2)}')
