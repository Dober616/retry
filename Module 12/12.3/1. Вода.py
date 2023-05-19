def about_water(x):

    print(f'Название: {name}\n'
          f'Производитель: {producer}\n'
          f'Цена: {price}')


producer = 'ВодЗавод'
name = 'КлирВотер'

for _ in range(3):
    price = int(input('Цена воды: '))
    about_water(price)