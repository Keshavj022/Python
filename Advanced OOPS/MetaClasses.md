# Metaclasses

## What is a Metaclass?
A metaclass is the class of a class. It defines how classes behave and can be used to customize class creation.

### Key Points :
- Metaclasses define the behavior of classes.
- They allow you to control the creation and behavior of classes.
### Example:
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class Dog(metaclass=Meta):
    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")
print(dog.name)
```