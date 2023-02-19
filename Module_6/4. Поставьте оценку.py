import random
positive = 0
negative = 0
while True:
    mark = random.randint(-100, 100)
    if mark > 0:
        positive += 1
    elif mark < 0:
        negative += 1
    else:
        break
print(f'Положительных оценок {positive}\n'
      f'Отрицательных оценок {negative}')
