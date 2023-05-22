def running_string(some_list, your_step):
    new_list = list()
    for element in some_list:
        new_list.insert(abs(your_step - some_list.index(element)), element)
    return new_list


original_list = [1, 4, -3, 0, 10]
step = 1
print(original_list)
print(running_string(original_list, step))
