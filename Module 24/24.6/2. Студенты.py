class Student:

    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.estimates = list()

    def middle_estimates(self):
        return sum(self.estimates) / len(self.estimates)


class Group:
    students_list = list()
    rating_dict = dict()

    def __init__(self, count):
        self.count = count

    def ordered_list(self):
        for i in range(self.count):
            name = input(f'Введите имя {i+1}-го студента: ')
            group = int(input(f'Введите группу {i+1}-го студента: '))
            mark_list = list()
            for _ in range(3):
                mark = int(input('Введите оценку: '))
                mark_list.append(mark)
            new_student = Student(name, group)
            new_student.estimates = mark_list
            self.students_list.append(new_student)
        return self.students_list

    def students_rating(self):
        for student in self.ordered_list():
            self.rating_dict[student.name] = student.middle_estimates()
        return sorted(self.rating_dict, key=lambda student: student[1])


new_group = Group(2)
for student in new_group.students_rating():
    print(student, new_group.rating_dict[student])
