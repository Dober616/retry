square = int(input('Введите площадь квартиры: '))
price = int(input('Введите стоимость квартиры: '))
if 80 < square < 100 and price >= 7000000:
    print('Вы можете позволить себе вариант подешевле')
elif square > 100 and price > 10**6:
    print('Вы можете себе позволить вариант подороже')
else:
    print('Хуй сосите')