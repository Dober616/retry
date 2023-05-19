my_string = input('Введите строку: ')
sym_list = [i for i in my_string]
sym_numm = int(input('Введите номер символа: '))
sym_numm -= 1
print(f'Символ слева: {sym_list[sym_numm - 1]}')
print(f'Символ справа: {sym_list[sym_numm + 1]}')
count = -1
for i in sym_list:
    if i == sym_list[sym_numm]:
        count += 1
print(f'Таких же символов в строке: {count}')