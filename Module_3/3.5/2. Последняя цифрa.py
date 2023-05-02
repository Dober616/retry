address = int(input('Введите адрес: '))
home_number = address % 10
flat_number = address // 10
print(f'Номер дома: {home_number}')
print(f'Номер квартиры: {flat_number}')