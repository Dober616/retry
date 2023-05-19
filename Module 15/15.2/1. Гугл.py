import random

nums_list = list()
nums_count = int(input('Количество чисел в списке: '))
for _ in range(nums_count):
    nums_list.append(random.randint(-50, 50))

print(nums_list)
max = 0
min = nums_list[0]

for numm in nums_list:
    if numm > max:
        max = numm
print(f'Самое большое число в списке: {max}')

for numm in nums_list:
    if numm < min:
        min = numm
print(f'Самое маленькое число в списке: {min}')