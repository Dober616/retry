people_count = 10 # int(input('Количество людей в очереди: '))
n = 0
for hour in range(12 + 1):
    print(f'{hour}-й час. Остались люди с номерами: ', end='')
    n += 1
    for number in range(n, people_count + 1):
        print(f"{number}, ", end='')
    print('')

