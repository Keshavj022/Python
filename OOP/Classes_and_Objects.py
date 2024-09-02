# Defining a class
class Dog:
    # Class attribute
    species = "Canis lupus familiaris"

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Molly", 3)

# Accessing class and instance attributes
print(f"{dog1.name} is {dog1.age} years old and belongs to the species {dog1.species}.")
print(f"{dog2.name} is {dog2.age} years old and belongs to the species {dog2.species}.")
