text = 'При*вет, как дела'
count = 0
for letter in text:
    count += 1
    if letter == '*':
        break
print(f'Символ * находится на позиции {count}')
