main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]
main.extend(first_company)
main.extend(second_company)
main.extend(third_company)
task_count = 0
for task in main:
    if task == 0:
        task_count += 1

print(f'Количество невыполненных задач стало {task_count}')