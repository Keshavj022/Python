class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)


class Dog(metaclass=Meta):
    def __init__(self, name):
        self.name = name


dog = Dog("Buddy")
print(dog.name)
