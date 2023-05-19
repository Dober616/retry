def numm_summ(x):
    summ = 0
    for i in range(1, x + 1):
        summ += i
    return summ


number = int(input('Конечное число: '))
print(f'Сумма чисел от 1 до {number} = {numm_summ(number)}')
print(f'Сумма чисел от 1 до {numm_summ(number)} = {numm_summ(numm_summ(number))}')
