my_list = list()
for number in range(10, 100):
    if number // 10 * number % 10 * 3 == number:
        my_list.append(number)

for i in my_list:
    print(i)
