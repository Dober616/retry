def string_action(a, b):
    if a.count('!') + a.count('?') > b.count('!') + b.count('?'):
        return a + b
    elif a.count('!') + a.count('?') < b.count('!') + b.count('?'):
        return b + ' ' + a
    else:
        return 'Ой...'


first_string = 'Привет!'  #input('Введите первую строку: ')
secnd_string = 'Как дела? Что делаешь?'  #input('Введите вторую строку: ')

print(string_action(first_string, secnd_string))
