n = int(input('Количество стульев: '))
summ = 0
for chair in range(1, n + 1, 5):

    print(f'Номер стула: {chair}')
    summ += chair
print(f'Сумма номеров стульев: {summ}')
