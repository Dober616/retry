import random

first_damage = [random.randint(50, 80) for _ in range(10)]
secnd_damage = [random.randint(30, 60) for _ in range(10)]
min_len_squad = min(len(first_damage), len(secnd_damage))
result = ['Погиб' if first_damage[i] + secnd_damage[i] < 100 else 'Выжил' for i in range(min_len_squad)]
print(f'Результаты битвы: {result}')
