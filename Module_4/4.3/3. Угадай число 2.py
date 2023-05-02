import random

guess = random.randint(1, 10)
question = int(input('Какое число я загадал: '))
if guess == question:
    print('Молодец, угадал!')
elif guess != question:
    print(f'Не угадал... Правильное число было {guess}')