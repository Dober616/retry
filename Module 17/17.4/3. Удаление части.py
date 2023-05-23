import random

n = 10 #int(input('Количество чисел в списке: '))
origin_list = [i for i in range(n)]
first_numm = random.randint(0, n)
secnd_numm = random.randint(first_numm, n)
print(first_numm, secnd_numm)
new_list = origin_list[first_numm:secnd_numm:]
print(new_list)