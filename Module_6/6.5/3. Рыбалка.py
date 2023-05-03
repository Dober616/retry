import random
summ_weight = 0
count = int(input('Сколько раз ходили с мешками?: '))
for i in range(count):
    weight = random.randint(3, 10)
    summ_weight += weight
print(f'Общий вес мешков {summ_weight}')
