temper = int(input('Сколько сейчас градусов: '))
distance = 0

while True:
    temper -= 1
    distance += 20
    if temper <= 15:
        break
print(f'Спортсмен пробежал {distance} метров')