import random

wake_up_time = int(input('Во сколько проснулся: '))
water = 0
calories = 0
for hour in range(wake_up_time, 23, 3):
    water += 1
    calories += random.randint(100, 200)
print(f'Петя съел {calories} калорий и выпил {water} литров воды')
