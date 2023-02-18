import random
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
print(a, b, c)

if a > b and a > c:
    print(f'Максимальное число: {a}')
elif b > a and b > c:
    print(f'Максимальное число: {b}')
elif c > a and c > b:
    print(f'Максимальное число: {c}')
