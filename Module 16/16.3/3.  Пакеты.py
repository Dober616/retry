import random

pack_count = int(input('Количество пакетов: '))
task_list = list()
lost_pack = 0
for i in range(pack_count):
    pack = list()
    print(f'Пакет номер {i + 1}')
    for bit in range(4):
        choice = random.randint(-1, 1)
        pack.append(choice)
        print(f'{bit + 1} бит: {choice}')
    if pack.count(-1) <= 1:
        task_list.extend(pack)
    else:
        lost_pack += 1

print(f'Полученное сообщение: {task_list}\n'
      f'Количество ошибок в пакете: {task_list.count(-1)}\n'
      f'Количество потерянных пакетов: {lost_pack}')
