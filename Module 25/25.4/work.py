class Pet:
    legs = 4
    has_tail = True
    def __str__(self):
        return f'Всего ног: {self.legs}, наличие хвоста: {self.has_tail}'

    def walk(self):
        print('Гуляем')


class Cat(Pet):
    def sound(self):
        print('Кошка говорит "Мяу"')


class Dog(Pet):
    def sound(self):
        print('Собака говорит "Гав"')


class Frog(Pet):
    has_tail = False
    def sound(self):
        print('Лягушка говорит "Ква"')

    def walk(self):
        print('Плавает')


cat = Cat()
dog = Dog()
frog = Frog()
print(cat)
print(dog)
print(frog)
cat.sound()
dog.sound()
frog.sound()
cat.walk()
frog.walk()