import random

my_list = [random.randint(-10, 10) for _ in range(1, 11)]
result_list = list()
for i in my_list:
    if i > 0 and i % 2 == 0:
        result_list.append(i)
print(my_list)
print(result_list)
