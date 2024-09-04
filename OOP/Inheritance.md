# Inheritance

## What is Inheritance?
Inheritance is a mechanism in which a new class (derived class) is created from an existing class (base class). The derived class inherits attributes and methods from the base class, allowing code reuse and the creation of hierarchical class structures.

### Key Points:
- Inheritance allows a class to inherit attributes and methods from another class.
- The super() function is used to call the constructor of the base class.
### Example:
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def details(self):
        return f"{self.name} is a {self.species}."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def details(self):
        return f"{self.name} is a {self.breed} {self.species}."

# Creating an object
dog = Dog("Buddy", "Golden Retriever")
print(dog.details())
```