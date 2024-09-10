class Dog:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


dog = Dog("Buddy")
print(dog.name)  # Outputs: Buddy
dog.name = "Max"
print(dog.name)  # Outputs: Max
