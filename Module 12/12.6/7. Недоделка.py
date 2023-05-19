import random


def rock_paper_scissors():
    choise_dict = {1: 'камень', 2: 'ножницы', 3: 'бумага'}
    opponent = random.randint(1, 3)
    player = int(input('Выберите камень(1), ножницы(2), бумага(3): '))
    print(f'Компьютер выбрал {choise_dict[opponent]}\nИгрок выбрал {choise_dict[player]}')
    if player == 1 and opponent == 2:
        return 'Победил игрок'
    elif player == 2 and opponent == 1:
        return 'Победил оппонент'
    elif player == 3 and opponent == 1:
        return 'Победил игрок'
    elif opponent == 3 and player == 1:
        return 'Победил оппонент'
    elif player == 3 and opponent == 2:
        return 'Победил оппонент'
    elif opponent == 2 and player == 3:
        return 'Победил игрок'
    elif opponent == player:
        rock_paper_scissors()


def guess_the_number():
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


def main_menu():
    action = int(input('Что делать будем?\n'
                       '1. Играть в камень ножницы бумага\n'
                       '2. Играть в угадай число\n'
                       '0. Выход\n'))
    if action == 1:
        for _ in range(3):
            print(rock_paper_scissors())
    elif action == 2:
        guess_the_number()
    elif action == 0:
        print('Приходите еще')
    else:
        print('Ошибка, выберите действие из списка')
        main_menu()


main_menu()
