import random

x = random.randint(1, 10)
y = random.randint(1, 10)
print(f'x: {x}')
print(f'y: {y}')

if x > y:
    print('x > y')
elif x < y:
    print('x < y')
else:
    print('x = y')