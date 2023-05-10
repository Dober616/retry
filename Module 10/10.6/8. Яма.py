n = 5
for col in range(n):
    for i in range(n, 0, -1):
        if i >= n - col:
            print(i, end='')
        else:
            print('.', end='')
    for y in range(n + 1):
        if y >= n - col:
            print(y, end='')
        else:
            print('.', end='')
    print('')
