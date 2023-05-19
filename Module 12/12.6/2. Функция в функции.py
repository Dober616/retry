def positive():
    print('Число положительное')


def negative():
    print('Число отрицательное')


def test(x):
    if x > 0:
        positive()
    elif x < 0:
        negative()
    else:
        print('Это же ноль')


number = int(input('Введите число: '))
test(number)
