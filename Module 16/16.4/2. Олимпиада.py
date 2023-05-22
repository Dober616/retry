participant_count = int(input('Количество участников: '))
people_in_team = int(input('Количество участников в команде: '))
team_list = list()
people_numm = 1
if participant_count % people_in_team == 0:
    for i in range(participant_count//people_in_team):

        temp_list = list()
        for y in range(people_in_team):
            temp_list.append(people_numm)
            people_numm += 1
        team_list.append(temp_list)
    print(f'Общий список команд: {team_list}')
else:
    print(f'{participant_count} участников невозможно поделить равные на команды по {people_in_team} человек')
