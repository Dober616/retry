n = 10
for i in range(n):
    print('\t')
    for y in range(0, -n, -1):
        print(i + y, end='\t')