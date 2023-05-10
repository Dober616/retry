height = int(input('Введите высоту пирамиды: '))
for i in range(1, height*2, 2):
    height -= 1
    print(' ' * height, '#' * i, ' ' * height)