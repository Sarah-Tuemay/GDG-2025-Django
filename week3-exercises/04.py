class Teacher:
    def work(self):
        print("Teachers work at school")

class Doctor:
    def work(self):
        print("Doctors work at the hospital")

careers = [Teacher(), Doctor()]

for career in careers:
    career.work()