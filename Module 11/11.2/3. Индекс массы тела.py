height = 1.75
weight = 80.3
imt = weight / (height ** 2)
print(f'Индекс массы тела: {round(imt, 2)}')
if imt < 18.5:
    print('Недобор')
elif imt < 25:
    print('Норма')
elif imt < 30:
    print('Избыточный вес')
else:
    print('Ожирение')