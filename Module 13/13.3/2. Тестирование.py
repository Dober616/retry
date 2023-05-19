import math

exp_numm = float(input('Введите число в эксп. форме: '))
x = 1


def exp_summ(numm, x):
    count = 0
    while x < 2:
        x += exp_numm
        count += 1
    return count


print(f'Количество прибавлений: {exp_summ(exp_numm, x)}')
