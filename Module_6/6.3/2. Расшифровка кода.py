def temp_numm(x):
    return number // deliver % 10


number = int(input('Введите огромное число: '))
summ = 0
deliver = 1
while True:
    summ += temp_numm(deliver)
    deliver *= 10
    if temp_numm(deliver) == 5:
        break
print(f'Сумма чисел равна {summ}')

