PLUGINS = dict()


def register(func):
    def wrapper(*args, **kwargs):
        PLUGINS[func.__name__] = func
        func(*args, **kwargs)
        print('Вроде работает...')
        return func(*args, **kwargs)
    return wrapper


@register
def greeting(name):
    return f'Hello {name}'


@register
def say_goodbye(name):
    return f'Goodbye {name}'


print(greeting('Кирилл'))
print(say_goodbye('Кирилл'))
print()
for i in PLUGINS:
    print(i, PLUGINS[i])
