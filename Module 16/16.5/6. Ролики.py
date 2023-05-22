import random
roller_count = 12
sizes_count = 12
sizes_list = [random.randint(36, 43) for _ in range(sizes_count)]
roller_list = [random.randint(36, 43) for _ in range(roller_count)]
print(roller_list, sizes_list)
people_count = 0
for i in roller_list:
    for y in sizes_list:
        if i == y:
            sizes_list.remove(y)
            people_count += 1


print(roller_list)
print(sizes_list)
print(f'Наибольшее количество людей, которые могут взять ролики: {people_count}')

