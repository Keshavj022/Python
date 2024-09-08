# Composition

## What is Composition?
Composition is a way to combine objects to build complex systems. It is a "has-a" relationship where one class contains an instance of another class.

### Key Points:
- Composition allows objects to contain other objects.
- It models a “has-a” relationship.
### Example:
```python
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

engine = Engine("V8")
car = Car("Mustang", engine)

print(car.model)       # Outputs: Mustang
print(car.engine.engine_type)  # Outputs: V8
```