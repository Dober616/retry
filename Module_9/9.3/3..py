text = 'Прыг скокЫ'
big = 0
small = 0
for letter in text:
    if letter == 'Ы':
        big += 1
    if letter == 'ы':
        small += 1

print(f'Больших букв "Ы": {big}\n'
      f'Маленьких букв "ы": {small}')