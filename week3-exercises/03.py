from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    def __init__(self):        
        self.ison = False
    def turn_on(self):
        self.ison = True
        return self.ison
    def turn_off(self):
        self.ison = False
        return self.ison

machine = WashingMachine()
print(machine.turn_on())
print(machine.turn_off())
