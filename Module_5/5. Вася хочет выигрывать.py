import random
first = random.randint(1, 3)
secnd = random.randint(1, 3)
third = random.randint(1, 3)

if first == secnd == third:
    print(3)
elif first == secnd or first == third or secnd == third:
    print(2)
else:
    print(1)