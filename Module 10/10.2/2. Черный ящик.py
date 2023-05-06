n = 10
for i in range(1, n + 1):
    print('')
    for y in range(1, n + 1):
        if y % 3 == 0:
            print(y, end='\t')
        else:
            print(i, end='\t')