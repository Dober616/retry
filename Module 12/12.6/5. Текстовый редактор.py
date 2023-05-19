text = input('Введите текст: ')


def count_letters(x):
    letter_count = 0
    digits_count = 0

    letter = input('Какую букву ищем: ')
    digit = input('Какую цифру ищем: ')
    for word in x:
        for some_letter in word:
            if some_letter == letter:
                letter_count += 1
            elif some_letter == digit:
                digits_count += 1
    print(f'Количество букв {letter}: {letter_count}\nКоличество цифр {digit}: {digits_count}')


count_letters(text)
