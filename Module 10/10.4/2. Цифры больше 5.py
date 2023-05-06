n = int(input('Количество чисел: '))
count = 0
numm_list = [x for x in range(n)]
for numm in numm_list:
    if numm > 5:
        count += 1
print(f'Чисел больше 5 в списке: {count}')
