def sorted_list(some_list):
    for _ in range(len(some_list)):
        for number in some_list[:len(some_list) -1]:
            current_index = original_list.index(number)
            next_index = current_index + 1
            if number > some_list[next_index]:
                some_list.pop(current_index)
                some_list.insert(next_index, number)
    return some_list


original_list = [1, 4, -3, 0, 10]
print(sorted_list(original_list))
