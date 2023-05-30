class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(
            f'Имя работника: {self.name}\n'
            f'Зарплата работника: {self.salary}'
        )


emp_1 = Employee('Tom', 10000)
emp_1.info()
emp_2 = Employee('Bob', 12000)
emp_2.info()
