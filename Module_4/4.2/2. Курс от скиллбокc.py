users_money = int(input('Состояние банковского счета: '))
course_price = 75000
if users_money >= course_price:
    users_money -= course_price
    print(f'Поздравляем, вы купили курс и у вас еще осталось {users_money} денег')
else:
    print(f'Денег не хватает, нужно еще подкопить {course_price - users_money} денег')