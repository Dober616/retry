class Dot:
    dot_count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Dot.dot_count += 1

    def info(self):
        print(f'Координаты точки({self.x}:{self.y})\nВсего создано точек: {self.dot_count}')


some_dot = Dot(3, 4)
some_dot.info()
new_dot = Dot()
new_dot.info()
ont = Dot(5, 7)
ont.info()

