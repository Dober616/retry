import random

first_numm = random.randint(1, 10)
secnd_numm = random.randint(1, 10)
print('First number: ', first_numm)
print('Second number: ', secnd_numm)
your_result = int(input('Input your result: '))
if your_result == first_numm + secnd_numm:
    print('Congratulations, correct answer')
else:
    print(f'Correct answer: {first_numm + secnd_numm}\nThink better')
