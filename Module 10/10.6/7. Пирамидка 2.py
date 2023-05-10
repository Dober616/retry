height = 5
number = 1
for i in range(1, height + 1):
    print(' ' * (height - i), end='')
    for _ in range(i):
        print(number, end=' ')
        number += 2
    print(' ', end='')
    print('')

