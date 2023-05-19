number = int(input('Введите число: '))


def reverse(x):
    result = 0
    while x != 0:
        result *= 10
        result += x % 10

        x //= 10
    return result


print(f'Число наоборот: {reverse(number)}')
