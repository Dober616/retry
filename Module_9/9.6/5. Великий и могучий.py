text = 'Здравствуйте, меня зовут Петр'
max_len = 0
longest_word = ''
for word in text.split(' '):
    len = 0
    for letter in word:
        if letter.isalpha():
            len += 1
    if len > max_len:
        max_len = len
        longest_word = word
print(f'Самое длинное слово {longest_word}, оно состоит из {max_len} букв')
