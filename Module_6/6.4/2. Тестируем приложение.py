import random


while True:
    test = random.choice([0, 1])
    if test == 1:
        print('Продолжать работать?: да')
    else:
        print('Продолжать работать?: нет')
        break
print('Приложение закрывается...')
