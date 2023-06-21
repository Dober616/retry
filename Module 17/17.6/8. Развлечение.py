import random

sticks_count = 10
sticks = dict()
for stick in range(1, sticks_count + 1):
    sticks[stick] = '|'
kicks_count = 3
for _ in range(kicks_count):
    left_i = random.randint(1, sticks_count)
    right_i = random.randint(left_i, sticks_count)
    for i in range(left_i, right_i + 1):
        sticks[i] = '.'

for i in sticks:
    print(sticks[i], end=' ')
