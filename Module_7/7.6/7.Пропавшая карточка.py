cards_count = int(input('Введите количество карточек: '))
cards_list = [i for i in range(1, cards_count + 1)]
for _ in range(cards_count - 1):
    number = int(input(f'Введите число от 1 до {cards_count}: '))
    cards_list.remove(number)
print(f'Потерявшаяся карточка: {cards_list[0]}')
