for row in range(1, 21):
    print('')
    for col in range(1, 51):
        if row == 1:
            print('-', end='')
        elif col == 1 or col == 50:
            print('|', end='')
        else:
            print(' ', end='')
