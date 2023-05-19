def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        return True


for i in range(5):
    numm = int(input('Введите число: '))
    if is_prime(numm):
        print('Простое число')
    else:
        print('Не является простым числом')