number = int(input('Введите число: '))
count = 1
while number // 10 > 0:
    count += 1
    number //= 10
print(f'В числе {count} цифр')
