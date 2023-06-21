import random

example_list = [random.randint(0, 2) for _ in range(10)]
print(f'Исходный список: {example_list}')
for i in example_list:
    if i == 0:
        example_list.remove(i)
        example_list.append(0)
print(f'Получившийся список: {example_list}')
zipped_list = [i for i in example_list if i != 0]
print(f'Чистый список: {zipped_list}')
