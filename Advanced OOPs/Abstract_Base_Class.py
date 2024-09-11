from abc import ABC, abstractmethod


# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


# Derived class 1
class Dog(Animal):
    def sound(self):
        return "Woof!"


# Derived class 2
class Cat(Animal):
    def sound(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print(dog.sound())  # Outputs: Woof!
print(cat.sound())  # Outputs: Meow!
