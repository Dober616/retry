container_count = 3 #int(input('Количество контейнеров: '))
container_list = list()
for _ in range(container_count):
    container = int(input('Вес контейнера: '))
    if container >= 200:
        print('Ошибка, контейнер не должен весить больше 200 тонн')
    else:
        container_list.append(container)

sorted_list = sorted(container_list)
print(f'Исходный список: {sorted_list}')

new_container = int(input('Вес нового контейнера: '))
for container in sorted_list:
    if new_container < sorted_list[0]:
        sorted_list.insert(0, new_container)
    else:
        while new_container < container:
            pass
        sorted_list.insert(sorted_list.index(container), new_container)

print(sorted_list)
