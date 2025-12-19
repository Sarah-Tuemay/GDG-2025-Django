class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def annual_salary(self):
        return 12 * self.salary

e1 = Employee("Sara", 120000)
print(e1.annual_salary())