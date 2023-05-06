n = 50
for i in range(21):
    print('')
    for y in range(51):
        if y == 51 // 2 and i != 21 // 2:
            print('|', end='')

        else:
            print(' ', end='')