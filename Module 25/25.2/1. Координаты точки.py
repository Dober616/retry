class Dot:
    def __init__(self, name, x, y):
        self.name = name
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        if x in range(1, 8):
            self.__x = x
        else:
            raise Exception('Недопустимая координата точки')

    def set_y(self, y):
        if y in range(1, 8):
            self.__y = y
        else:
            raise Exception('Недопустимая координата точки')

    def get_x(self, __x):
        return self.__x

    def get_y(self, __y):
        return self.__y

    def __str__(self):
        return f'Координаты точки {self.name}: {self.__x, self.__y}'

my_dot = Dot('Крестик', 4, 5)
new_dot = Dot('Нолик', 1, 6)

print(my_dot, new_dot)