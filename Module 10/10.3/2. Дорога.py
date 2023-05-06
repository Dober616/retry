step = 3

for row in range(1, 21):
    print('')
    step += 1

    for col in range(1, 51):

        if row == 21 // 2:
            print('-', end='')
        elif col == 50 // 2 - step:
            print('/', end='')
        elif col == 50 // 2 + step:
            print('\\', end='')
        elif col == 50 // 2:
            print("|", end='')
        else:
            print(' ', end='')
