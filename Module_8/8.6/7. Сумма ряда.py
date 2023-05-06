count = int(input('Введите число N: '))
for n in range(count + 1):
    elem = -1 ** n * (1 / 2 ** n)
    print(f'Elem = {elem}')
