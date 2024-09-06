class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_species(cls, species_name):
        cls.species = species_name


Dog.set_species("Canis familiaris")
dog1 = Dog("Buddy", 5)
print(dog1.species)


class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b


print(MathOperations.add(10, 20))  # Outputs: 30
