def number(iter):
    number = int(input(f'Введите {iter}-ое число адреса: '))
    if 0 > number or number > 255:
        print('Ошибка, номер должен быть больше 0 и меньше 256')
        while 0 > number or number > 255:
            number = int(input(f'Введите {iter}-ое число адреса: '))
    return number


ip_parts = dict()
for i in range(4):
    ip_parts[i] = number(i + 1)

print(f'IP-address: {ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{ip_parts[3]}')
