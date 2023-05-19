word_list = [input('Введите слово: ') for _ in range(3)]
text = input('Введите текст: ')
text_list = [word for word in text.split(' ')]
print(text_list)
for word in word_list:
    count = 0
    for other_word in text_list:
        if word == other_word:
            count += 1
    print(f'Слово "{word}" повторяется в тексте {count} раз')
