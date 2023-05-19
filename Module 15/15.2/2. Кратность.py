import random

n = int(input('Введите количество чисел в списке: '))
multipl = int(input('Введите кратность: '))
numm_list = [random.randint(1, 100) for _ in range(n)]
print(numm_list)
index_summ = 0
for number in numm_list:
    if number % multipl == 0:
        print(f'Индекс числа {number} равен {numm_list.index(number)}')
        index_summ += numm_list.index(number)
print(f'Сумма индексов: {index_summ}')