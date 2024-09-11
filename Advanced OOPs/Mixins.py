# Defining Mixins
class WalkMixin:
    def walk(self):
        return "Walking"


class TalkMixin:
    def talk(self):
        return "Talking"


# Class using Mixins
class Person(WalkMixin, TalkMixin):
    pass


# Creating an object of the class
person = Person()
print(person.walk())  # Outputs: Walking
print(person.talk())  # Outputs: Talking
