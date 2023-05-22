first_class = [i for i in range(160, 177, 2)]
secnd_class = [i for i in range(162, 180, 3)]
print(first_class, secnd_class)

first_class.extend(secnd_class)
print(sorted(first_class))