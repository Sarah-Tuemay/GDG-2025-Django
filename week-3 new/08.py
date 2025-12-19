class Animal:
    def make_sound(self):
        print("Animal")
class Cat(Animal):
    def make_sound(self):
        print("Cat")

c1 = Cat()
a1 = Animal()
c1.make_sound()
a1.make_sound()
