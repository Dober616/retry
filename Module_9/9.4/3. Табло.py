n = 50# int(input('Введите конечное число: '))
print('-=-', end='')
for number in range(0, n + 1, 10):
    print(f'{number}', end='-=-')