def summa_n(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result


number = int(input('Введите число: '))
print(f'Я знаю, что сумма чисел от 1 до {number} равна {summa_n(number)}')