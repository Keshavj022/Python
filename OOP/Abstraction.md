# Abstraction

## What is Abstraction?
Abstraction is the concept of hiding the complex reality while exposing only the necessary parts. It helps in reducing programming complexity and effort. In Python, abstraction is typically achieved through abstract classes and interfaces.

### Key Points:

- Abstraction simplifies complex systems by modeling classes appropriate to the problem.
- It is implemented using abstract classes and methods.
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

# Creating objects
dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())
```