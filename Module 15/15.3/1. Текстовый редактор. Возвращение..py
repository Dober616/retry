my_string = 'шурупы:гвозди:гайки' #input('Введите строку:')
find_symbol = input('Какой символ меняем: ')
new_symbol = input('На что меняем: ')

print(f'Исходная строка: {my_string}')
sym_list = [i for i in my_string]
count = 0
for sym in sym_list:
    i = sym_list.index(sym)
    if sym == find_symbol:
        sym_list[i] = new_symbol
        count += 1
print('Окончательная строка: ', end='')
for i in sym_list:
    print(i, end='')

print(f'\nВсего замен: {count}')
