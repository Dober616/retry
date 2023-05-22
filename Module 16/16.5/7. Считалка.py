def drop_the_numm(some_list, start_ind, step):
    drop_ind = abs(start_ind - step)
    while drop_ind > len(some_list):
        drop_ind -= len(some_list)
    return drop_ind - 1


def game(some_list, step, start_ind):
    while len(some_list) > 1:
        print(some_list)
        drop_numm = some_list[drop_the_numm(some_list, start_ind, step)]
        print(f'Вылетает номер {drop_numm}')

        start_ind = some_list[some_list.index(drop_numm)]
        some_list.remove(drop_numm)
        # print(f'Начало отсчета с номера {some_list[start_ind - 1]}')

    return some_list


players_count = 5 #int(input('Количество игроков: '))
game_step = 7 #int(input('Какой номер выбывает: '))
players_list = [i for i in range(1, 6)]

print(f'Остался игрок под номером {game(players_list, 7, start_ind=0)}')
