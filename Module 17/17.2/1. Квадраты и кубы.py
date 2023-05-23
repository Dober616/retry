left_limit = int(input('Введите левую границу: '))
right_limit = int(input('Введите правую границу: '))
squares = [i ** 2 for i in range(left_limit, right_limit + 1)]
qubes = [i ** 3 for i in range(left_limit, right_limit + 1)]
print(f'Список кубов чисел в диапазоне от {left_limit} до {right_limit}: {qubes}')
print(f'Список квадратов чисел в диапазоне от {left_limit} до {right_limit}: {squares}')
