# Interfaces

## What is an Interface?
An interface defines a contract for what a class can do, without specifying how it should be done. In Python, we use Abstract Base Classes (ABCs) to implement interfaces.

### Key Points:
- Interfaces define the required methods that a class must implement.
- In Python, ABCs are used to create interfaces.
- Interfaces provide a way to achieve abstraction in Python.

### Example:
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car started"

    def stop(self):
        return "Car stopped"

car = Car()
print(car.start())  # Outputs: Car started
print(car.stop())   # Outputs: Car stopped
```