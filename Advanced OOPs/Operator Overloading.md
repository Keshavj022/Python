# Operator Overloading

## What is Operator Overloading?
Operator overloading allows you to define how operators like `+`, `-`, `*`, etc., behave when applied to objects of a class.

### Key Points:
- Operator overloading allows you to define custom behavior for operators.
- The __add__ method is used to define behavior for the + operator.
### Example:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v3)  # Outputs: (4, 6)
```