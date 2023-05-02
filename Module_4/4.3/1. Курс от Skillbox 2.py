course_price = 75000
how_much_money = int(input('Сколько денег у вас есть: '))
if how_much_money >= course_price:
    print(f'Congratulations! You bought the course, and you have {how_much_money - course_price}')
else:
    print(f'Not enough {course_price - how_much_money} money')
