a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
my_list = [i for i in range(a, b + 1) if i % 3 == 0]
print(my_list)
