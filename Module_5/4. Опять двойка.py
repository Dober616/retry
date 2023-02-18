import random

rating = random.randint(2, 5) #int(input('Что получил по математике?: '))
if rating == 2 or rating == 3:
    print('Плохо. Иди учись!')
else:
    print('Молодец, можешь отдохнуть')
