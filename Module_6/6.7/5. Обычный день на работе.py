import random
hour = 0
tasks = 0
name = 'Максим'
wife_call = 0
print('Начался восьмичасовой рабочий день')
while hour < 8:
    hour += 1
    print(f'{hour}-й час')
    hour_task = random.randint(0, 5)
    tasks += hour_task
    print(f'{name} выполнит {hour_task} задач')
    call = random.choice([True, False])
    if call:
        wife_call += 1
print(f'{name} выполнил {tasks} задач')
if wife_call > 0:
    print('А еще надо зайти в магазин')



