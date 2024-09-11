# Multi-level Inheritance
class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)


dog = Dog("Buddy")
print(dog.name)  # Outputs: Buddy


# Multiple Inheritance
class A:
    def method_a(self):
        return "Method from class A"


class B:
    def method_b(self):
        return "Method from class B"


class C(A, B):
    pass


c = C()
print(c.method_a())  # Outputs: Method from class A
print(c.method_b())  # Outputs: Method from class B
