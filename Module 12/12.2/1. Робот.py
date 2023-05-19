def greeting():
    print('Привет!')
    print('Добро пожаловать!')

while True:
    quest = input('Зайдете? (да/нет): ')
    if quest.lower() == 'да':
        greeting()
    print('Следующий...')
