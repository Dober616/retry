violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56],
                  ['Halo', 4.9], ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20],
                  ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83]
]


songs_count = int(input('Количество песен: '))
song_time = 0
for i in range(songs_count):
    song_name = input(f'Название {i + 1}-й песни: ')
    for i in violator_songs:
        if song_name in i:
            song_time += i[1]

print(f'Общее время добавленных песен: {round(song_time, 2)}')