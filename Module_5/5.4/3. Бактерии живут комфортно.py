import random

temperature = random.randint(-20, 120)
print(f'{temperature}')
if 0 < temperature > 100:
    print('Некомфортная среда для бактерий')
else:
    print('С бактериями все в порядке')
    