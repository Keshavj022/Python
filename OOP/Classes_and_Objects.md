# Classes and Objects

## What is a Class?
A class is a blueprint or prototype that defines the variables and methods common to all objects of a certain kind. It is a logical entity that defines the behavior and attributes of an object.

## What is an Object?
An object is an instance of a class. It represents the real-world entity in your program.

### Example:
```python
class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Molly", 3)

print(f"{dog1.name} is {dog1.age} years old and belongs to the species {dog1.species}.")
print(f"{dog2.name} is {dog2.age} years old and belongs to the species {dog2.species}.")