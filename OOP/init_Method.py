# Defining a class with an __init__ method
class Dog:
    def __init__(self, name, age):
        # Initializing instance attributes
        self.name = name
        self.age = age

    def details(self):
        return f"{self.name} is {self.age} years old."


# Creating an object
dog = Dog("Buddy", 5)

# Accessing the details method
print(dog.details())
