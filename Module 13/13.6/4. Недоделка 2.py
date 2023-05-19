def digit_count(x):
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count


def exchange(x):
    last_digit = x % 10
    first_digit = x // 10 ** (digit_count(x) - 1)
    middle_digits = x % 10 ** (digit_count(x) - 1) // 10
    return last_digit * 10 ** (digit_count(x) - 1) + middle_digits * 10 + first_digit


first_numm = 123 #int(input('Введите первое число(трехзначное): '))
while digit_count(first_numm) != 3:
    print('Ошибка, число должно быть трехзначное')
    first_numm = int(input('Введите первое число(трехзначное): '))
secnd_numm = 1234 # int(input('Введите второе число(четырехзначное): '))
while digit_count(secnd_numm) != 4:
    print('Ошибка, число должно быть четырехзначное')
    secnd_numm = int(input('Введите второе число(четырехзначное): '))


print(f'Измененное первое число: {exchange(first_numm)}')
print(f'Измененное второе число: {exchange(secnd_numm)}')
print(f'Сумма получившихся чисел равна {exchange(first_numm) + exchange(secnd_numm)}')
