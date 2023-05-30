import random


class Warrior:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        War.warriors_list.append(self)

    def info(self):
        print(f'У {self.name} осталось {self.health} очков здоровья')


class War:

    warriors_list = list()

    def kick(self):
        defence = random.choice(self.warriors_list)
        defence.health -= 20
        for warrior in self.warriors_list:
            warrior.info()


war1 = Warrior('Егор', 200)
war2 = Warrior('Макс')

battle = War()
while True:
    battle.kick()
    if war1.health == 0:
        print(f'Победил игрок {war2.name}')
        break
    elif war2.health == 0:
        print(f'Победил игрок {war1.name}')
        break

