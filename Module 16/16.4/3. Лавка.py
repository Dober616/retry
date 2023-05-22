goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print(f'Текущий ассортимент: {goods}')
new_fruit = list()
fruit_name = input('Название нового фрукта: ')
new_fruit.append(fruit_name)
fruit_price = int(input('Цена нового фрукта: '))
new_fruit.append(fruit_price)
goods.append(new_fruit)
print(f'Новый ассортимент: {goods}')
for fruit in goods:
    fruit[1] = round(fruit[1] * 1.08, 2)
print(f'Новый ассортимент: {goods}')
