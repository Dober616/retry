import random
employee_count = int(input('Количество работников: '))
salary_list = [random.choice([0, random.randint(10000, 20000)]) for _ in range(employee_count)]
employee = 1
for salary in salary_list:
    print(f'Зарплата {employee}-го сотрудника: {salary}')
    employee += 1

for salary in salary_list:
    if salary <= 0:
        salary_list.remove(salary)

employee = 1
print(f'Количество работников: {len(salary_list)}')
for salary in salary_list:
    print(f'Зарплата {employee}-го сотрудника: {salary}')
    employee += 1

print(f'Максимальная зарплата: {max(salary_list)}')
print(f'Минимальная зарплата: {min(salary_list)}')
