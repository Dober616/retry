class CanFly:
    def __init__(self, height=0, speed=0):
        self.set_height(height)
        self.set_speed(speed)

    def set_height(self, height):
        if height >= 0:
            self.__height = height
        else:
            print('Объект не может лететь на отрицательной высоте')

    def get_height(self):
        return self.__height

    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed
        else:
            print('Объект не может лететь с отрицательной скоростью')

    def get_speed(self):
        return self.__speed

    def take_off(self):
        pass

    def fly(self):
        pass

    def ground(self):
        self.set_height(0)
        self.set_speed(0)


class Rocket(CanFly):
    def __init__(self):
        super().__init__()

    def take_off(self):
        self.set_speed(1000)
        self.set_height(500)
        print(f'Ракета летит. Высота {self.get_height()}, скорость {self.get_speed()}')
        self.ground()
        self.explosion()

    def ground(self):
        self.set_speed(0)
        self.set_height(0)
        print('Ракета приземлилась и попала в цель...')

    def explosion(self):
        print('Бабах!!!')


class Butterfly(CanFly):
    def __init__(self):
        super().__init__()

    def take_off(self):
        self.set_height(1)
        self.set_speed(0.5)
        print(f'Бабочка взлетела! Текущая высота {self.get_height()}, текущая скорость {self.get_speed()}')
        self.ground()

    def ground(self):
        self.set_height(0)
        self.set_speed(0)
        print(f'Бабочка Приземлилась! Текущая высота {self.get_height()}, текущая скорость {self.get_speed()}')


missle = Rocket()
missle.take_off()
ttt = Butterfly()
ttt.take_off()
