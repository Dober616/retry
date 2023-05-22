def the_game(count, numm):
    players_list = [i for i in range(1, count + 1)]
    start_numm = 1
    while len(players_list) > 1:
        print(f'Текущий круг людей: {players_list}')
        drop_index = abs(players_list.index(start_numm) - numm)
        while drop_index > len(players_list):
            drop_index -= len(players_list)
        print(f'Выбывает {players_list[drop_index]}')
        players_list.pop(drop_index)
        start_numm = abs(drop_index - len(players_list))


players_count = int(input('Количество игроков: '))
game_numm = int(input('Какой номер выбывает: '))

the_game(players_count, game_numm)
