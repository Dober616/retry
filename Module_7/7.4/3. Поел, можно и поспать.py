wake_up = int(input('Во сколько проснулся: '))
calories = 0
for hour in range(wake_up, 23):
    eat = int(input(f'{hour} часa(ов). Съедено калорий: '))
    calories += eat
    if calories >= 2000:
        print(f'Чувак уснул в {hour} часа(ов)\nСъедено {calories} калорий')
        break
print(f'Чувак уснул в 23 часа\nСъедено {calories} калорий')

