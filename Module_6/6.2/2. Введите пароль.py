real_password = '235'
password = input('Введите пароль: ')
while password != real_password:
    password = input('Пароль неверный, повторите ввод: ')
print('Поздравляю, пароль верный!')

