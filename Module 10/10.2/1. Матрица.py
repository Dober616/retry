n = 5
for i in range(1, n + 1):
    print('')
    for y in range(1, n + 1):
        if i % 2 == 0:
            print(i, end='\t')
        else:
            print(y, end='\t')
