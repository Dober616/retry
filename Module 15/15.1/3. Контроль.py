import random

employee_list = [random.randint(1, 50) for _ in range(4)]
print(employee_list)
find_employee = int(input('Кого ищем: '))
if find_employee in employee_list:
    print('Сотрудник на работе')
else:
    print('Такого сотрудника сегодня нет')
