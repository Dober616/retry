import random

guess = random.randint(1, 10)
answer = int(input('Ответ сына: '))
if answer == guess:
    print('Угадал, можешь идти погулять')
else:
    print(f'Будешь весь день делать уроки, а число было {guess}')