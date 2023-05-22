shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200],
        ['седло', 2700]]

temp_list = list()
detail = input('Введите название детали: ')
temp_list.append(detail)
price = int(input('Стоимость детали: '))
temp_list.append(price)
shop.append(temp_list)
detail_count = 0
total_price = 0
for i in shop:
    if detail in i:
        detail_count += 1
        total_price += i[1]

print(f'Количество деталей: {detail_count}\nОбщая стоимость: {total_price}')
