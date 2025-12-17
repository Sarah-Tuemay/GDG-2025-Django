from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculateSalary(self, taxrate, salary):
        pass

class PartTimeEmployee(Employee):
    def calculateSalary(self, taxrate, salary):
        caclSalary = salary - (salary * taxrate)
        return caclSalary

# e1 = Employee() this will generate a typeError: 'Can't instantiate abstract class Employee without an implementation for abstract method 'calculateSalary' '
# print(e1.calculateSalary()) 

e2 = PartTimeEmployee()
print(e2.calculateSalary(0.15, 40000))