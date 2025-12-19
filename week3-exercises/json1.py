import json
class Student:
    def __init__(self, name, age, attendance):
        self.name=name
        self.age = age
        self.attendance = attendance

    def todict(self):
        return {
            "name": self.name,
            "age": self.age,
            "attendance": self.attendance,
            }
    def tojson(self):
        temp = json.dumps(self.todict())
        return temp

        
student1 = Student("abebe", 27, True)
print(student1.todict())
print(student1.tojson())