import random

points = random.randint(250, 300)
medal = random.choice([True, False])
print(f'Баллы: {points}\nМедаль: {medal}')
if medal is True and points >= 290:
    print('Поздравляем, вы поступили')
else:
    if medal is False:
        print('Эх, еще бы медаль. Пока поступать рано...')
    elif points < 290:
        print('Баллов не хватает...')