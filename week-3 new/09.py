class Vehicle:
    def __init__(self, year, brand):
        self.year = year
        self.brand = brand
    def info(self):
        print(f"year: {self.year} brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, year, brand, model):
        super().__init__(year, brand)
        self.model = model
    def info(self):
        print(f"year: {self.year} brand: {self.brand} model: {self.model}")

c1 = Car(2002, "Toyota", "B4zx")
c1.info()
