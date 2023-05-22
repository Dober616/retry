container_count = int(input('Количество контейнеров: '))
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

if new_container > container_list[len(container_list) - 1]:
    sorted_list.append(new_container)
else:
    for container in sorted_list:
        if new_container <= container:
            sorted_list.insert(sorted_list.index(container), new_container)
            break
print(f'{sorted_list}\nНомер, который получит новый контейнер {sorted_list.index(new_container) + 1}')
