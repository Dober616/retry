def is_simple(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        return True


count_nums = 6
simple_nums = []
for _ in range(count_nums):
    numm = int(input('Введите число: '))
    if is_simple(numm):
        simple_nums.append(numm)
print(f'Количество простых чисел: {len(simple_nums)}')

