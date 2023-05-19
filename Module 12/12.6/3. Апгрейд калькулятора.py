def sum(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result


def max_numm(n):
    max = 0
    while n != 0:
        temp = n % 10
        if temp > max:
            max = temp
        n //= 10
    return max


def min_numm(n):
    min = n % 10
    while n != 0:
        temp = n % 10
        if temp < min:
            min = temp
        n //= 10
    return min


number = int(input('Введите число: '))
question = int(input('Что делаем с числом? (сумма - 0, максимальное - 1, минимальное - 2): '))
if question == 0:
    print(f'Сумма цифр равна {sum(number)}')
elif question == 1:
    print(f'Максимальная цифра: {max_numm(number)}')
elif question == 2:
    print(f'Минимальная цифра: {min_numm(number)}')