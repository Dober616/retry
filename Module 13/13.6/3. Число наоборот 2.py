def reverse(x):
    result = 0
    while x != 0:
        result *= 10
        result += x % 10

        x //= 10
    return result


first_numm = int(input('Введите первое число: '))
secnd_numm = int(input('Введите второе число: '))

print(f'Первое число наоборот: {reverse(first_numm)}')
print(f'Второе число наоборот: {reverse(secnd_numm)}')
summ = reverse(first_numm) + reverse(secnd_numm)
print(f'Сумма получившихся чисел = {summ}')
print(f'Сумма чисел наоборот = {reverse(summ)}')
