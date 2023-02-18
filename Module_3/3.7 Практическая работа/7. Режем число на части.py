number = 1234 #int(input('Введите четырехзначное число: '))
a = number % 10
b = number % 100 // 10
c = number % 1000 // 100
d = number // 1000

print(a, b, c, d)