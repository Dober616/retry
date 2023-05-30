class Robot:
    def __init__(self, model):
        self.model = model

    def operate(self):
        print('Робот начинает работу')

    def self_return(self):
        print(f'Робот {self.model} возвращается на базу')


class Cleaner(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.capacity = 0

    def operate(self):
        print(f'Робот {self.model} начинает уборку')
        while self.capacity < 10:
            self.capacity += 1
            print('Робот собрал 1 единицу мусора')
        print('Резервуар для мусора заполнен')
        self.self_return()


class Warrior(Robot):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon
        self.battery = 10

    def operate(self):
        print(f'Робот {self.model} выехал на обход территории и готов атаковать врага с помощью {self.weapon}\n'
              f'Заряд батареи {self.battery}')
        while self.battery != 0:
            self.battery -= 1
            print(f'Робот объехал территорию, остаток заряда батареи {self.battery}')
        self.self_return()


class Submarine(Warrior):
    def __init__(self, model, weapon):
        super().__init__(model, weapon)


r2d2 = Warrior('Боевой робот', 'plazma gun')
puppo = Cleaner('Уборщик')

r2d2.operate()
puppo.operate()
b12 = Submarine('Boat', "Торпеда")
b12.operate()



