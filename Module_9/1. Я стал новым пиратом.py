count = 0
scream = 'карамба'
for i in range(3):
    word = input('Введите слово: ')
    if word.lower() == scream:
        count += 1

print(f'В команду берем {count} пиратов')
