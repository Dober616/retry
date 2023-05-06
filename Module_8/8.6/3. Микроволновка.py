cook_time = int(input('Введите время приготовления еды: '))
for time in range(cook_time, -1, -1):
    if time == 0:
        print('Еда готова, забирайте уже')
    else:
        question = input(f'Осталось {time} секунд. Готовы ли вы забрать еду? ')
        if question == 'да':
            print('Ваша еда готова. Можете забрать.')
        elif question == 'нет':
            pass


