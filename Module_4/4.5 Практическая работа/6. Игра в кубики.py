import random

Kostya_points = 0
Owner_points = 0
for _ in range(10):
    Kostya = random.randint(1, 6)
    Owner = random.randint(1, 6)
    if Kostya >= Owner:
        points = Kostya - Owner
        print(f'Разность равна {points}\nИгрок платит')
        Owner_points += points
    else:
        points = Kostya + Owner
        print(f'Сумма равна {points}\nВладелец платит')
        Kostya_points += points

print(f'Очки Кости {Kostya_points}\n'
      f'Очки владельца {Owner_points}')

