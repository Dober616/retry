file_size = int(input('Размер файла: '))
network_speed = int(input('Скорость интернет соединения: '))
seconds = file_size // network_speed
for i in range(0, file_size, network_speed):

    print(f'Осталось {seconds} секунд. Скачано {i} мегабайт из {file_size} ({i * 100 // file_size}%)')
    seconds -= 1
print('Скачивание файла завершено!')