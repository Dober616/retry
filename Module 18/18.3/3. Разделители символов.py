name = input('Введите Имена и Фамилии через запятую: ')
age = input('Введите возрасты через пробел: ')
people_names = name.split(', ')
people_ages = age.split()
for i in range(3):
    print(f'С Днем рождения тебя {people_names[i]}! Тебе уже {people_ages[i]} лет')
