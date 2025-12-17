from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Bus(Transport):
    def move(self):
        print("The car is moving")

class Train(Transport):
    def move(self):
        print("The train is moving")

