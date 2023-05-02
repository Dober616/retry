for raw in range(6):
    for col in range(10):
        if raw == 0 or raw == 5:
            print('-', end='')
        elif col == 0 or col == 9:
            print('|', end='')
        else:
            print('0', end='')
    print()



