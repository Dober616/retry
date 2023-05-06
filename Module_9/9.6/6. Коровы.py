import random

milk = 0
milk_count = 0
cow_list = [random.choice(['a', 'b']) for _ in range(10)]
print(cow_list)
for cow in cow_list:
    milk += 2
    if cow == 'a':
        milk_count += milk
print(milk_count)
