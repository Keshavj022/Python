# Defining a base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def details(self):
        return f"{self.name} is a {self.species}."


# Defining a derived class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def details(self):
        return f"{self.name} is a {self.breed} {self.species}."


# Creating an object of the derived class
dog = Dog("Buddy", "Golden Retriever")

# Accessing methods from the derived class
print(dog.details())
