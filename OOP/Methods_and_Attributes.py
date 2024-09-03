# Defining a class with methods
class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to get the dog's details
    def details(self):
        return f"{self.name} is {self.age} years old."

    # Method to simulate barking
    def bark(self, sound="Woof!"):
        return f"{self.name} says {sound}"


# Creating an object
dog = Dog("Buddy", 5)

# Accessing methods
print(dog.details())
print(dog.bark())
print(dog.bark("Bark! Bark!"))
