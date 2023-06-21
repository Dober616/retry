n = 10
numm_list = [i for i in range(n)]
print(numm_list)
my_list = [1 if numm_list.index(i) % 2 == 0 else i % 5 for i in numm_list]
print(my_list)
