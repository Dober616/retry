start = int(input('Введите начальное число: '))
finish = int(input('Введите конечное число: '))
multiplicity = int(input('Укажите кратность: '))
my_list = [i for i in range(start, finish) if i % multiplicity == 0]
print(my_list)
