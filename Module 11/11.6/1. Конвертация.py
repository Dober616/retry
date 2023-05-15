euro_price = float(input('Стоимость покупки в евро: '))
dollar_price = euro_price * 1.25
rub_price = dollar_price * 60.87
print('Стоимость в долларах: ', round(dollar_price, 2))
print('Стоимость в рублях: ', round(rub_price, 2))