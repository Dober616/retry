import random

marks = [random.randint(3, 5) for _ in range(10)]
perfect = 0
good = 0
satisfactorily = 0
for mark in marks:
    if mark == 5:
        perfect += 1
    elif mark == 4:
        good += 1
    else:
        satisfactorily += 1
if perfect > good and perfect > satisfactorily:
    print('Отличников больше')
elif good > perfect and good > satisfactorily:
    print('Хорошистов больше')
elif satisfactorily > perfect and satisfactorily > good:
    print('Троечников больше')

