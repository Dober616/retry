def palindrome(some_word):
    left_part = some_word[0:len(some_word) // 2:]
    right_part = some_word[0:len(some_word) // 2:]
    return left_part, right_part

word = 'mamam' #input('Введите слово: ')
word_2 = 'mama'
print(palindrome(word))
print(palindrome(word_2))
