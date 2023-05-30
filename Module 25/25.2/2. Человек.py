class Human:
    __count = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Human.__count += 1

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception('Имя принимает только строковое значение!')

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            raise Exception('Возраст должен быть между 1 и 100')

    def get_age(self):
        return self.__age

    def __str__(self):
        return f'Имя человека: {self.__name}, ему {self.__age} лет'

    def get_count(self):
        return self.__count


egor = Human('Egor', 33)
tom = Human('Tom', 34)
print(egor)
print(tom)
print(tom.get_count())

