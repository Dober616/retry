def decorator_up(func):
    def wrapper():
        print('</---------\>')
        func()
        print('<\________/>')
    return wrapper


def decorator_down(func):
    def wrapper():
        print('Томат')
        print(func())
        print('Салат')
        return func()
    return wrapper

@ decorator_up
@ decorator_down
def sandwich():
    return ('--ветчина--')

sandwich()