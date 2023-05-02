import random

money = random.randint(50, 140)
cheese_price = 60
milk_price = 20
icecream_price = 10

if money >= cheese_price:
    print('На сыр хватает')
    money -= cheese_price
    if money >= milk_price:
        print('И на молоко хватает')
        money -= milk_price
        if money >= icecream_price:
            print('О, и на мороженку хватило!')
        else:
            print('Но на мороженое не хватило...')
    else:
        print('А на молоко не хватило...')
else:
    print('Даже на сыр не хватает ...')
