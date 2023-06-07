def decorator(func):
    def wrapped(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapped


@decorator
def greeting(name):
    print(f'Привет {name}! Хаварю?')


greeting('Кирилл')
