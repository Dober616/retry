word = input('Введите слово: ')
additional_symbol = input('Введите дополнительный символ: ')
double = [i * 2 for i in word]
additional_list = [i * 2 + additional_symbol for i in word]
print(f'Список удвоенных символов: {double}')
print(f'Склейка с дополнительным символом: {additional_list}')
