class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine


engine = Engine("V8")
car = Car("Mustang", engine)

print(car.model)  # Outputs: Mustang
print(car.engine.engine_type)  # Outputs: V8
