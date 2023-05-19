my_numbers = [3, 7, 5]
degree = (2, 3, 4)
while True:
    new_numm = int(input('Введите новое число: '))
    my_numbers.append(new_numm)
    print(f'Текущий список чисел: {my_numbers}')
    for number in my_numbers:
        for i in degree:
            print(number ** i, end=' ')
        print()
