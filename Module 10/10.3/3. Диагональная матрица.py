n = 5
step = 0
temp = 5
for i in range(n):
    print('')
    temp -= 1
    for y in range(n):
        if y < temp:
            print(0, end='\t')
        elif y == temp:
            print(1, end='\t')
        else:
            print(2, end='\t')