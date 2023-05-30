class Potato:
    states = {0: 'отсутствует', 1: 'росток', 2: 'зеленая', 3: 'созрела'}

    def __init__(self, number):
        self.number = number
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1

    def info(self):
        print(f'Картошка {self.number} в стадии {self.states[self.state]}')

    def is_ripe(self):
        if self.state == 3:
            return True


class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(number) for number in range(1, count + 1)]

    def grow_all(self):
        while not all([Potato.is_ripe(potato) for potato in self.potatoes]):
            print('Картошка созревает')
            for potato in self.potatoes:
                potato.grow()
                potato.info()
        print('Поздравляем, вся картошка созрела, можно собирать!')


ttt = Garden(5)
ttt.grow_all()
