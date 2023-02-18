import random
points = random.randint(250, 300)
place = random.randint(1, 30)
if place > 10:
    print('Место так себе')
else:
    if points >= 290:
        print('Поздравляем, вы поступили')
    else:
        print('Баллов не хватает')

