class Potato:
    grow_states = {0: 'отсутствует', 1: 'росток', 2: 'зеленая', 3: 'клубни'}

    def __init__(self, number):
        self.number = number
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        # self.info()

    def info(self):
        print(f'Картошка {self.number} сейчас в стадии {self.grow_states[self.state]}')
        # print(f'Картошка {self.number} сейчас в стадии {Potato.grow_states[self.state]}')

    def is_ripe(self):
        if self.state == 3:
            return True


class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(number) for number in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает...')
        while not self.all_ripe():
            for potato in self.potatoes:
                potato.grow()
                potato.info()

    def all_ripe(self):
        if all([potato.is_ripe() for potato in self.potatoes]):
            print('Поздравляем, вся картошка созрела, можно собирать')
            return True
        else:
            return False


some_garden = Garden(5)
some_garden.grow_all()
