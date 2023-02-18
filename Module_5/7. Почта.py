# с 8 до 22
# 14 - 15
# 10 - 18
import random

time = random.randint(0, 23)
print(time)
if time in range(8, 22) and time != 14 and time != 10 and time != 18:
    print('Вы можете забрать посылку')
else:
    print('Хуй вам')