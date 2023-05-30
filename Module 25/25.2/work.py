class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return f'Имя: {self.__name}, возраст: {self.__age}'

    def get_count(self):
        return self.__count

    def set_age(self, age):
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')

    def get_age(self):
        return self.__age


misha = Person('Миша', 38)
egor = Person('Егор', 2)
misha.set_age(85)
print(misha.get_age())

print(misha, egor)
print(egor.get_count())
