x, y = 8, 10

while True:
    print(f'Марсоход находится на позиции ({x}:{y})')
    move = input('Куда двигамся: ')
    if move.lower() == 'e':
        if y < 20:
            y += 1
        else:
            y = y
            print('Вы уперлись в стену')
    elif move.lower() == 'd':
        if y > 0:
            y -= 1
        else:
            y = y
    elif move.lower() == 's':
        x -= 1
    elif move.lower() == 'f':
        x += 1