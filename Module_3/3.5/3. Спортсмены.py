first_runner_distance = 2040
lap_distance = 100

laps = first_runner_distance // lap_distance
print(f'Бегун пробежал {laps} кругов')
print(f'Дополнительно пробежал {first_runner_distance % lap_distance} метров')
