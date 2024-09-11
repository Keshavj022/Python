# Abstract Base Classes (ABC)

## What is an Abstract Base Class (ABC)?
An Abstract Base Class (ABC) is a class that cannot be instantiated and is used to define a common interface for its derived classes. It typically contains one or more abstract methods, which must be implemented by subclasses.

### Why use ABCs?
- ABCs enforce a standard interface across multiple derived classes.
- They are useful when you want to ensure that certain methods are implemented in the subclasses.

### Key Points:
- ABCs are created by inheriting from abc.ABC.
- Subclasses must implement all abstract methods defined in the ABC.
### Example:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.sound())  # Outputs: Woof!
print(cat.sound())  # Outputs: Meow!