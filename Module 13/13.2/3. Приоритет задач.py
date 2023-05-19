tasks_count = int(input('Введите количество задач: '))


def numeral_count(x):
    most_important_task = 0
    for _ in range(tasks_count):
        task_numm = int(input('Введите число: '))
        if task_numm > most_important_task:
            most_important_task = task_numm
    return most_important_task


print(f'Наиболее важная задача № {numeral_count(tasks_count)}')
