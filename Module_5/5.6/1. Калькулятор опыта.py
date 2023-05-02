import random
points = random.randint(1, 10000)
skill = 1
if 1000 <= points < 2500:
    skill = 2
elif 2500 <= points < 500:
    skill = 3
elif points >= 5000:
    skill = 4

print(f'Ваш уровень: {skill}')
