import random


class Carma:
    karma_points = 0
    day = 0

    def my_life(self):
        while self.karma_points < 500:
            self.day += 1
            print(f'Наступил {self.day}-й день...')
            self.one_day()

    def one_day(self):

        new_points = random.randint(1, 7)
        my_list = [new_points, DrunkError, KillError, DepressionError]
        action = random.choice(my_list)
        if action == new_points:
            self.karma_points += new_points
            print(f'Выпало {new_points} очков кармы\n'
                  f'Текущие очки кармы: {self.karma_points}')
        else:
            action.write_log()



class Exception:
    def action(self):
        print('Ошибочка вышла')


class DrunkError(Exception):
    def write_log(self):
        with open('karma.log', 'w') as log_file:
            log_file.write('Ошибочка вышла')
        print('Ошибочка')


class KillError(Exception):
    def write_log(self):
        with open('karma.log', 'w') as log_file:
            log_file.write('Ошибочка вышла')
        print('Ошибочка')


class DepressionError(Exception):
    def write_log(self):
        with open('karma.log', 'w') as log_file:
            log_file.write('Ошибочка вышла')
        print('Ошибочка')




budda = Carma()
budda.my_life()
