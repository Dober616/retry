text = 'Мы должны принести это кольцо в Мордор!'
vovels = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
vovel_text_list = [i for i in text if i in vovels]
print(f'Гласные буквы текста: {vovel_text_list}')
print(f'Количество гласных букв в тексте: {len(vovel_text_list)}')