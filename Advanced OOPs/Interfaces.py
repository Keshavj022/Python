from abc import ABC, abstractmethod


# Interface (using ABC)
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Class implementing the interface
class Car(Vehicle):
    def start(self):
        return "Car started"

    def stop(self):
        return "Car stopped"


car = Car()
print(car.start())  # Outputs: Car started
print(car.stop())  # Outputs: Car stopped
