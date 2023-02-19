guess = int(input('Загадайте число от 0 до 100: '))
start = 0
finish = 100
count = 0

while True:
    count += 1
    answer = round((start + finish) / 2)
    if answer < guess:
        start = answer
    elif answer > guess:
        finish = answer
    else:
        print(f'Загаданное число: {answer}\nКоличество попыток: {count}')
        break

