wright_code = 777

while True:
    print('Компьютер заблокирован. Вернешь скейт - скажу код разблокировки!')
    code = int(input('Введите код разблокировки: '))
    if code == wright_code:
        break
print('Код верный завершаю работу...')