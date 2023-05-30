class Ship:
    def __init__(self, model):
        self.__model = model

    def sail(self):
        print(f'{self.__model} корабль плывет')

    def __str__(self):
        return f'Модель корабля: {self.__model}'


class WarShip(Ship):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def attack(self):
        print(f'Корабль атакует врага с помощью оружия {self.weapon}')


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.capacity = 0

    def load(self, weight):
        self.capacity += weight
        print(f'Груз погружен, корабль везет {self.capacity} тонн груза')

    def unload(self, weight):
        if weight <= self.capacity:
            self.capacity -= weight
            print(f'Корабль разгрузился, текущий груз {self.capacity} тонн')
        else:
            print('Так нет на корабле столько груза...')


warrior = WarShip('Авианосец', 'Пулемет')
warrior.sail()
warrior.attack()

cargo = CargoShip('Грузовой')
cargo.load(10)
cargo.sail()
cargo.unload(8)
