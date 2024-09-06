# Class Methods and Static Methods

## Class Methods
Class methods are methods that are bound to the class and not the object of the class. They can modify class-level data.

### Example:
```python
class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_species(cls, species_name):
        cls.species = species_name

# Calling class method
Dog.set_species("Canis familiaris")

dog1 = Dog("Buddy", 5)
print(dog1.species)
```
### Static Methods
Static methods do not have access to self or cls. They are used to perform tasks that do not depend on class or instance variables.
```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(10, 20))  # Outputs: 30
```

### Key Points:

- Class methods are defined with the @classmethod decorator.
- Static methods are defined with the @staticmethod decorator.
