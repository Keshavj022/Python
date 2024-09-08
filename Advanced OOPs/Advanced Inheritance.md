# Advanced Inheritance

## Multi-level Inheritance
In multi-level inheritance, a class inherits from a class that is already a derived class.

### Example:
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)

dog = Dog("Buddy")
print(dog.name)  # Outputs: Buddy
```
## Multiple Inheritance
In multiple inheritance, a class can inherit from more than one base class.

### Example:
```python
class A:
    def method_a(self):
        return "Method from class A"

class B:
    def method_b(self):
        return "Method from class B"

class C(A, B):
    pass

c = C()
print(c.method_a())  # Outputs: Method from class A
print(c.method_b())  # Outputs: Method from class B
```

### Key Points:
- Multi-level inheritance involves a chain of inheritance across multiple levels.
- Multiple inheritance allows a class to inherit from multiple base classes.