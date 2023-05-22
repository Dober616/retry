def party(guest_list):
    print(f'Сейчас на вечеринке {len(guest_list)} человек')
    while True:
        question = input('Гость пришел или ушел: ')
        if question == 'пришел':
            if len(guest_list) == 6:
                print('На вечеринке уже 6 человек. Мест больше нет')
            else:
                guest_name = input('Введите имя гостя: ')
                guest_list.append(guest_name)
                print(f'Привет {guest_name}\nСейчас на вечеринке {len(guest_list)} человек')
        elif question == 'ушел':
            guest_name = input('Введите имя гостя: ')
            guest_list.remove(guest_name)
            print(f'Пока {guest_name}\nСейчас на вечеринке {len(guest_list)} человек')
        elif question == 'пора спать':
            print('Вечеринка окончена, всем спокойной ночи')
            break
        else:
            print('Ошибка, повторите ввод')
            party(guest_list)


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
party(guests)
