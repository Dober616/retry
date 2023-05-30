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


class Student(Human):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def study(self):
        print(f'Студент идет в университет {self.university} учиться')

    def __str__(self):
        info = super().__str__()
        return info


class Employee(Human):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.company = company
        self.salary = salary
        self.money = 0

    def work(self):
        self.money += self.salary
        print(f'Работник пошел работать в {self.company} и заработал {self.salary} денег, теперь у него {self.money}')

    def __str__(self):
        return f'Работник {self.get_name()} работает в {self.company} и получает зарплату {self.salary}. ' \
               f'Ему {self.get_age()} лет'


# egor = Human('Egor', 33)
# tom = Human('Tom', 34)
# jim = Employee('Джим', 25, 'Газпром', 10000)
# jim.work()
tim = Student('Тим', 18, 'МГУ')
print(tim)
tim.study()
# print(jim)
# print(egor)
# print(tom)
# print(tom.get_count())

