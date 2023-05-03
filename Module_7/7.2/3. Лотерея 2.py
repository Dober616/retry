def digit_count(x):
    count = 1
    while x // 10 != 0:
        count += 1
        x //= 10

    return count


for number in [345, 19, 87, 1020, 421]:
    if digit_count(number) == 3 and number % 5 == 0:
        print(f'Билет № {number} выигрышный')
