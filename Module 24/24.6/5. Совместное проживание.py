import random


class Human:
    count = 0

    def __init__(self, name, satiety=50, energy=50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def info(self):
        print(f'День: {self.count}-й\n'
              f'Сытость: {self.satiety}\n'
              f'Энергия: {self.energy}\n'
              f'Деньги: {House.money}\n'
              f'Еда: {House.food}')

    def eat(self):
        print('Едим...')
        self.satiety += 20
        House.food -= 20

    def work(self):
        print('Работаем...')
        House.money += 50
        self.satiety -= 20
        self.energy -= 20

    def rest(self):
        print('Отдыхаем...')
        self.energy += 20
        self.satiety -= 10

    def food_shopping(self):
        print('Идем в магазин...')
        if House.money >= 50:
            House.food += 50
            House.money -= 50
            self.energy -= 10
        else:
            House.food += House.money
            House.money = 0
            self.energy -= House.money // 5

    def play(self):
        print('Играем...')
        self.satiety -= 10
        self.energy += 10

    def death(self):
        if self.satiety < 0 or self.energy < 0:
            print('Ну все, помер Боб')
            return True

    def one_day(self):
        self.count += 1
        action = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif House.food < 10:
            self.food_shopping()
        elif House.money < 50:
            self.work()
        elif action == 1:
            self.work()
        elif action == 2:
            self.eat()
        else:
            self.play()
        self.info()


class House:
    money = 0
    food = 50


bob = Human('Боб')
for _ in range(365):
    bob.one_day()
    if bob.death():
        break
