import random


def competitions(team_a, team_b):
    result = list()
    for i in range(len(first_team)):
        if first_team[i] > secnd_team[i]:
            result.append(first_team[i])
        else:
            result.append(secnd_team[i])
    return result


first_team = [round(random.uniform(5, 10), 2) for _ in range(10)]
secnd_team = [round(random.uniform(5, 10), 2) for _ in range(10)]
print(f'Игроки первой команды: {first_team}')
print(f'Игроки второй команды: {secnd_team}')

print(f'Результаты соревнований: {competitions(first_team, secnd_team)}')
