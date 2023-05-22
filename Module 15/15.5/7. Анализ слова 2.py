def palindrome(some_word):
    left_part = some_word[0:len(some_word) // 2]
    if len(some_word) % 2 == 0:
        right_part = some_word[-1: len(some_word) // 2 - 1: -1]
    else:
        right_part = some_word[-1: len(some_word) // 2: -1]
    if left_part == right_part:
        print(f'Слово {some_word} является палиндромом')
    else:
        print(f'Слово {some_word} не является палиндромом')


word = 'mamam' #input('Введите слово: ')
word_2 = 'mama'
word_3 = 'qwerty'
word_4 = 'qwert'
palindrome(word)
palindrome(word_2)
palindrome(word_3)
palindrome(word_4)
