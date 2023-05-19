def amplitude(x, y):
    count = 0
    while x > y:
        x -= x * 8.4 / 100
        count += 1
    return count


start_ampl = float(input('Введите начальную амплитуду: '))
stop_ampl = float(input('Введите амплитуду остановки: '))
print(f'Маятник считается остановившимся через {amplitude(start_ampl, stop_ampl)} колебаний')
