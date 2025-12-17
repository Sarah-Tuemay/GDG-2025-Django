from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def claculateSalary(self, taxrate, salary):
        pass

class FullTimeEmployee(Employee):
    def claculateSalary(self, taxrate, salary):
        caclSalary = salary - (salary * taxrate)
        return caclSalary


e1 = FullTimeEmployee()
print(e1.claculateSalary(0.15, 300000))