number = 1
count = 0


def min_numm(x, y):
    while x > 0:
        x /= 2
        y += 1
    return x, y


print(min_numm(number, count))
