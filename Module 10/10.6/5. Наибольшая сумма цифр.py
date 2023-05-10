import random


def digits_summ(x):
    summ = 0
    while x > 0:
        summ += x % 10
        x //= 10
    return summ


n = 5
max_summ = 0
for _ in range(n):
    number = random.randint(1, 100)
    print(number)
    if digits_summ(number) >= max_summ:
        max_summ = digits_summ(number)
print('Наибольшая сумма цифр: ', max_summ)
