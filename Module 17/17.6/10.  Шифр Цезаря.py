def caesar_code(text, step):
    new_message = ''
    for i in text:
        if i in alfabet:
            temp = alfabet.index(i) + step
            if temp <= len(alfabet) - 1:
                i = alfabet[temp]
            else:
                temp -= len(alfabet)
                i = alfabet[temp]
        else:
            i = i
        new_message += i
    return new_message


alfabet = [chr(letter) for letter in range(ord('а'), ord('я') + 1)]

message = 'вот такие пироги'
print(alfabet)
print(caesar_code(message, step=3))

