nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
open_list = [number for some_list in nice_list for under_list in some_list for number in under_list]
print(open_list)
