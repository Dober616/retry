def my_films(some_list):
    film = input('Введите название фильма: ')
    action = int(input('Какое действие совершить с фильмом (0 - удалить, 1 - добавить, 2 - переместить): '))
    if action == 0:
        film_list.remove(film)
    elif action == 1:
        film_list.append(film)
    elif action == 2:
        place = int(input('На какое место поставить фильм: '))
        film_list.remove(film)
        film_list.insert(place, film)
    else:
        print('Ошибка, попробуйте еще раз...')
        return my_films(some_list)
    return film_list


film_list = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

print(my_films(film_list))
