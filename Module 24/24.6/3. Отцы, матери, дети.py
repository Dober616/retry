class Parent:
    child_list = list()

    def __init__(self, name, status, age):
        self.name = name
        self.age = age
        self.status = status

    def info(self):
        print(f'Имя родителя: {self.name}, '
              f'возраст: {self.age}, '
              f'дети: {[i.name for i in self.child_list]}'
              )

    def feed(self, child):
        print(f'Родитель {self.name} кормит ребенка {child.name}')
        child.hungry -= 1

    def play(self, child):
        print(f'Родитель {self.name} играет с ребенком {child.name}')
        child.stress -= 1

    def action(self):
        for child in self.child_list:
            if child.hungry > 0:
                while child.hungry > 0:
                    print(f'Родитель {self.name} кормит {child.name}\nУровень голода уменьшается на 1 пункт')
                    self.feed(child)
            elif child.stress > 0:
                while child.stress > 0:
                    print(f'Родитель {self.name} играет с {child.name}\nУровень усталости снижается на 1 пункт')
                    self.play(child)


class Child:
    def __init__(self, name, age, stress=0, hungry=0):
        self.name = name
        self.age = age
        self.stress = stress
        self.hungry = hungry
        Parent.child_list.append(self)

    def info(self):
        print(f'Имя ребенка: {self.name}, '
              f'возраст: {self.age}, '
              f'усталость: {self.stress}, '
              f'голод: {self.hungry}'
              )

    def homework(self):
        self.hungry += 1
        self.stress += 1
        print(f'{self.name} делает домашнее задание...\n'
              f'Уровень голода повысился до {self.hungry}\n'
              f'Уровень стресса повысился до {self.stress}')


bob = Child('Bob', 15)
lisa = Child('Lisa', 13)
for _ in range(3):
    lisa.homework()
    bob.homework()

elena = Parent('Elena', 'mother', 60)
oleg = Parent('Oleg', 'father', 61)
print(elena.info())
print(oleg.info())
elena.action()