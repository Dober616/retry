names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list = list()
for name in names_list:
    if names_list.index(name) % 2 == 0:
        new_list.append(name)
print(new_list)
