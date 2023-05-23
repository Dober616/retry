start_numm = int(input('Введите начальное число: '))
finish_numm = int(input('Введите конечное число: '))
my_numbers = [i for i in range(start_numm, finish_numm + 1) if i % 2 == 0]
print(f'Список четных чисел: {my_numbers}')