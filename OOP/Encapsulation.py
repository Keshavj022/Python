# Defining a class with encapsulation
class Dog:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    # Public method to get dog's name
    def get_name(self):
        return self.__name

    # Public method to set dog's age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

    def details(self):
        return f"{self.__name} is {self.__age} years old."


# Creating an object
dog = Dog("Buddy", 5)

# Accessing public methods
print(dog.get_name())
dog.set_age(6)
print(dog.details())
