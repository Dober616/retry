def symmetry(some_list):
    print(f'Последовательность: {number_list}')
    temp_list = some_list
    count = 0
    while number_list[:len(temp_list) // 2] != number_list[:len(temp_list) // 2:-1]:
        add_numbers.insert(0, temp_list[0])
        temp_list.pop(0)
        count += 1
    return count


# number_count = int(input('Введите количество чисел в последовательности: '))
number_list = [1, 2, 3, 4, 5]
add_numbers = list()
print(f'Нужно дописать {symmetry(number_list)} чисел')
print(f'Сами числа: {add_numbers}')

