def new_card(some_list):
    latest_card = 0
    for card in some_list:
        if card > latest_card:
            latest_card = card
    return latest_card


def remove_card(some_list):
    for card in some_list:
        if card == new_card(some_list):
            some_list.remove(card)
    return some_list


card_count = int(input('Количество видеокарт: '))
card_list = list()
for _ in range(card_count):
    card_list.append(int(input('Введите модель карты: ')))
print(f'Старый список видеокарт: {card_list}')
print(f'Новый список видеокарт {remove_card(card_list)}')
