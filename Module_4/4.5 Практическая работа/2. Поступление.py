rus = int(input('Введите количество баллов по русскому языку: '))
math = int(input('Введите количество баллов по математике: '))
inf = int(input('Введите количество баллов по информатике: '))
if sum([rus, math, inf]) >= 270:
    print('Поздравляем, вы поступили на бюджет!')
else:
    print('Баллов пока не хватает, копите на платное')