# Mixins

## What is a Mixin?
A Mixin is a class that provides methods to other classes through multiple inheritance. Mixins are not meant to be instantiated on their own but are used to "mix" additional functionality into other classes.

### Why use Mixins?
- **Code Reuse**: Mixins allow you to reuse code across different classes without inheriting all the features of the parent class.
- **Modular Design**: You can break down the functionality of a class into separate, smaller mixins.
### Key Points:
- Mixins allow for modular, reusable pieces of functionality.
- They are used with multiple inheritance to add specific functionality to classes.
### Example:
```python
class WalkMixin:
    def walk(self):
        return "Walking"

class TalkMixin:
    def talk(self):
        return "Talking"

class Person(WalkMixin, TalkMixin):
    pass

person = Person()
print(person.walk())  # Outputs: Walking
print(person.talk())  # Outputs: Talking
```