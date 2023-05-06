import random

debtors_count = int(input('Введите количество должников: '))
debt_summ = 0
debtor_list = [random.randint(2000, 5000) for _ in range(debtors_count)]
for i in range(0, debtors_count + 1, 5):
    debt_summ += debtor_list[i]
    print(f'Должник под номером {i} должен {debtor_list[i]}')
print(f'Общая сумма долга: {debt_summ}')
