import random

soldiers = int(input('Солдат в шеренге: '))
count = 10
pushups_count = 0
for soldier in range(soldiers-4, 0, -4):
    print(f'Солдат {soldier}, сколько статей в уставе?')
    answer = random.randint(1, 10)
    print(answer)
    if answer != count:
        pushups = soldier * 10
        print(f'Ответ неверный, солдат, {pushups} отжиманий!')
        pushups_count += pushups
    else:
        print('Молодец, солдат, правильный ответ!')

print(f'Всего отжиманий: {pushups_count}')
