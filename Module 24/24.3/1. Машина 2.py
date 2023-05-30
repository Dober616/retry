import random


class Car:
    color = None
    price = None
    max_speed = None
    current_speed = None

    def info(self):
        print(f'Цвет: {self.color}\n'
              f'Цена: {self.price}\n'
              f'Максимальная скорость: {self.max_speed}\n'
              f'Текущая скорость: {self.current_speed}')

    def set_max_speed(self, speed):
        self.max_speed = speed

    def set_current_speed(self, speed):
        self.current_speed = speed


toyota = Car()
toyota.color = 'Красный'
toyota.price = '1000000'
toyota.max_speed = random.randint(180, 240)
toyota.current_speed = 0

toyota.info()
toyota.set_max_speed(250)
toyota.info()
toyota.set_current_speed(random.randint(100, 240))
toyota.info()