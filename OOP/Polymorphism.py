class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def sound(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def sound(self):
        return f"{self.name} says Meow!"


# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.sound())
print(cat.sound())
