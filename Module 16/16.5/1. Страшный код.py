a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
print(f'Количество цифр 5 при первом объединении: {a.count(5)}')
for i in a:
    if i == 5:
        a.remove(i)
a.extend(c)
print(f'Количество цифр 3 при втором объединении: {a.count(3)}')
print(f'Итоговый список: {a}')
