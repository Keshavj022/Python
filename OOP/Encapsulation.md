# Encapsulation

## What is Encapsulation?
Encapsulation is the practice of bundling the data (attributes) and the methods that operate on the data into a single unit or class. It restricts access to certain attributes and methods, making the class more secure and less prone to errors.
### Key Points:
- Encapsulation helps protect the internal state of the object.
- Private attributes are denoted by a double underscore (__).
### Example:
```python
class Dog:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

    def details(self):
        return f"{self.__name} is {self.__age} years old."

# Creating an object
dog = Dog("Buddy", 5)

print(dog.get_name())
dog.set_age(6)
print(dog.details())
```