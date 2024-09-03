# The `__init__` Method

## What is `__init__`?
The `__init__` method is a special method in Python classes. It is known as the constructor and is automatically called when an object is created. It is used to initialize the attributes of the object.

### Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        return f"{self.name} is {self.age} years old."

# Creating an object
dog = Dog("Buddy", 5)
print(dog.details())
```
