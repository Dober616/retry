writer = 'Пушкин'
good_marks = 0
bed_marrs = 0
for _ in range(5):
    question = input('Кто написал "Евгений Онегин"? ')
    if question == writer:
        good_marks += 1
        break
    else:
        bed_marrs += 1

print(f'Хороших оценок: {good_marks}\n'
      f'Плохих оценок: {bed_marrs}')

