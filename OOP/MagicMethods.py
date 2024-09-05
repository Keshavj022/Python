class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __add__(self, other):
        return f"{self.name} and {other.name} are friends."

    def __len__(self):
        return len(self.name)


# Creating objects
dog1 = Dog("Buddy", 5)
dog2 = Dog("Molly", 3)

print(dog1)
print(dog1 + dog2)
print(len(dog1))
