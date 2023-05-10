n = 10
for col in range(n + 1):
    print('')
    for row in range(n * 2 + 1):
        if row == 0 or row == n * 2:
            print('|', end='')
        elif col == 0 or col == n:
            print('-', end='')
        else:
            print(' ', end='')
