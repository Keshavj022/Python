# Magic Methods (Dunder Methods)

## What are Magic Methods?
Magic methods are special methods that start and end with double underscores (`__`). They are also known as "dunder" methods. These methods allow you to define the behavior of your objects in response to built-in Python operations, such as arithmetic operations, comparisons, and string representations.

### Key Points:

- Magic Methods define how objects of a class interact with Python’s built-in operations.
- Common magic methods include __init__, __str__, __add__, and __len__.
### Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __add__(self, other):
        return f"{self.name} and {other.name} are friends."

    def __len__(self):
        return len(self.name)

# Creating objects
dog1 = Dog("Buddy", 5)
dog2 = Dog("Molly", 3)

print(dog1)
print(dog1 + dog2)
print(len(dog1))