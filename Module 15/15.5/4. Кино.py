films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
film_count = int(input('Сколько фильмов хотите добавить: '))
my_list = list()
for _ in range(film_count):
    film = input('Введите название фильма: ')
    if film in films:
        my_list.append(film)
    else:
        print('Такого фильма в базе нет')
print(f'Мой список фильмов: {my_list}')
