class Unit:
    def __init__(self, hp):
        self.hp = hp

    def get_damage(self, damage):
        print(f'Юнит получает урон {damage}')
        self.hp -= damage
        print(f'Теперь у юнита {self.hp} здоровья')


class Soldier(Unit):
    def __init__(self, hp):
        super().__init__(hp)


class Civillian(Unit):
    def __init__(self, hp):
        super().__init__(hp)

    def get_damage(self, damage):
        print(f'Юнит получает урон {damage * 2}')
        self.hp -= damage * 2
        print(f'Теперь у юнита {self.hp} здоровья')


sold = Soldier(100)
civi = Civillian(100)
sold.get_damage(20)
civi.get_damage(20)