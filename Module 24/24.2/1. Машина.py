import random


class Car():
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0


toyota = Car()
bmw = Car()
vw = Car()
toyota.max_speed = random.randint(100, 200)
bmw.max_speed = random.randint(100, 200)
vw.max_speed = random.randint(100, 200)

print(toyota.max_speed)
print(bmw.max_speed)
print(vw.max_speed)