# Property Decorators

## What are Property Decorators?
Property decorators (`@property`) allow you to define methods that act like attributes, providing getter, setter, and deleter functionalities.

### Key Points:
- Property decorators allow you to control access to instance variables with getter, setter, and deleter methods.
### Example:
```python
class Dog:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

dog = Dog("Buddy")
print(dog.name)  # Outputs: Buddy
dog.name = "Max"
print(dog.name)  # Outputs: Max
```