# Attributes and Methods

## What are Attributes?
Attributes are variables that belong to an object or class. They represent the state or data of the object.

## What are Methods?
Methods are functions that belong to a class and define behaviors of an object. They operate on the attributes of the class.

---
### Example:
```python
class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, sound="Woof!"):
        return f"{self.name} says {sound}"

# Creating an object
dog = Dog("Buddy", 5)

# Accessing attributes and methods
print(dog.name)
print(dog.bark())