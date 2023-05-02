import random

course_price = 75000
student_money = random.randint(50000, 100000)
if course_price <= student_money:
    student_money -= course_price
    if student_money < 5000:
        student_money += 1000
        print(f'Вам сделана скидка 1000 рэ! У вас теперь {student_money} денег')
    else:
        print(f'Осталось {student_money} денег')

else:
    print(f'Не хватает еще {course_price - student_money} денег')