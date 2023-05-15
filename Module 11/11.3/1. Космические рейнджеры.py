import math

summ_chatle = int(input('Сколько всего чатлов: '))
cr = summ_chatle / 2200
print(f'Это {cr} CR\n'
      f'На эту сумму можно купить {math.floor(cr / 0.5)} космических корабля')
