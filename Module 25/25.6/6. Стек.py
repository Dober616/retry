class Steck:
    def __init__(self):
        self.__st = list()

    def __str__(self):
        return str(self.__st)

    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()


my_st = Steck()
for i in range(5):
    my_st.push(i)
print(my_st)
for _ in range(3):
    my_st.pop()
print(my_st)