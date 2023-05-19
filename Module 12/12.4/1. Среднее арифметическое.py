def middle(a, b):
    result = 0
    count = 0
    for number in range(a, b + 1):
        result += number
        count += 1
    return result / count


a = int(input('Введите левую границу: '))
b = int(input('Введите правую границу: '))
if a > b:
    print('Левая граница должна быть меньше правой')
else:
    print(f'Среднее арифметическое: {middle(a, b)}')

