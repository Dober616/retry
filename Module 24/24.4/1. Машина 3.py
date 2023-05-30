class Car:

    def __init__(self, name: str, color: str, current_speed: int, max_speed: int):
        self.name = name
        self.color = color
        self.current_speed = current_speed
        self.max_speed = max_speed

    def info(self):
        print(
            f'Марка машины: {self.name}\n'
            f'Цвет: {self.color}\n'
            f'Текущая скорость: {self.current_speed}\n'
            f'Максимальная скорость: {self.max_speed}'
        )


toyota = Car('Тойота', 'Красный', 0, 200)
bmw = Car('BMW', 'Черный', 0, 240)

toyota.info()
bmw.info()
