# Polymorphism

## What is Polymorphism?
Polymorphism allows methods to do different things based on the object it is acting upon. This means a single function or method can work in different ways depending on the context.

### Key Points:

- Polymorphism allows the same interface to be used for different data types.
- It is commonly implemented through method overriding.
### Example:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def sound(self):
        return f"{self.name} says Meow!"

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.sound())
print(cat.sound())
```