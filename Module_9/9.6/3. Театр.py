rows = int(input('Количество рядов: '))
sits_in_row = int(input('Количество мест в ряду: '))
meters_between_rows = int(input('Количество метров между рядами: '))
for row in range(rows):
    print('=' * sits_in_row + '*' * meters_between_rows + '=' * sits_in_row)
