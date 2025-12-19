class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"name: {self.name} age: {self.age}")

p1 = Person("sara", 22)
p1.introduce()
