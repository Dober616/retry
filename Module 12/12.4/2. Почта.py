def post(a, b, c, d, e, f, g):
    print(f'Фамилия: {a}\nИмя: {b}\nСтрана проживания: {c}\nГород: {d}'
          f'\nУлица: {e}\nДом: {f}\nКвартира: {g}')

for _ in range(3):
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    country = input('Введите страну проживания: ')
    city = input('Введите город: ')
    street = input('Введите улицу: ')
    house = input('Введите дом: ')
    flat = input('Введите номер квартиры: ')
    post(surname, name, country, city, street, house, flat)