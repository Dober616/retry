import random

numm = int(input('Введите число: '))
summ = 0
while numm <= 0:
    summ += numm
    numm = random.randint(-10, 10)
print(summ)