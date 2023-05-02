import random
x = random.randint(-5, 5)
y = 0
if x > 0:
    y = x - 12
elif x == 0:
    y = 5
elif x < 0:
    y = x * 2

print(x, y)