def eqv(x, y, z):
    if z - (x + y) < 1e-15:
        return True
    else:
        return False


first_numm = float(input('Введите первое число: '))
secnd_numm = float(input('Введите второе число: '))
third_numm = float(input('Введите третье число: '))

print(eqv(first_numm, secnd_numm, third_numm))
