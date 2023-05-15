bet = float(input('Размер ставки: '))
coeff = float(input('Коэффициент: '))
win = round(bet * coeff, 2)
print(f'Потенциальный выигрыш: {win}')