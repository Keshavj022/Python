def greet():
    """This function prints a greeting message."""
    print("Hello, welcome to Python!")


# Calling the function
greet()


def greet(name):
    """This function greets the person whose name is passed as an argument."""
    print(f"Hello, {name}! Welcome to Python!")


# Calling the function with an argument
greet("Alice")


def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b


# Calling the function and storing the result in a variable
result = add(5, 3)
print(result)


def greet(name="Guest"):
    """This function greets the person with a default name if no name is provided."""
    print(f"Hello, {name}! Welcome to Python!")


# Calling the function without an argument
greet()

# Calling the function with an argument
greet("Alice")


def describe_person(name, age, city):
    """This function prints a description of a person."""
    print(f"{name} is {age} years old and lives in {city}.")


# Using keyword arguments
describe_person(age=30, city="New York", name="Alice")


def sum_all(*args):
    """This function returns the sum of all arguments."""
    return sum(args)


# Calling the function with different numbers of arguments
print(sum_all(1, 2, 3))
print(sum_all(4, 5, 6, 7, 8))


def print_details(**kwargs):
    """This function prints details provided as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calling the function with keyword arguments
print_details(name="Alice", age=30, city="New York")

# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(5, 3))

# Lambda function to return the square of a number
square = lambda x: x ** 2
print(square(4))
