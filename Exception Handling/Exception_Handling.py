# Basic try-except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

# Multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Error: That's not a valid number!")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

# Else and Finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")


# Raising an exception
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return "Access granted."


try:
    print(check_age(16))
except ValueError as e:
    print(f"Error: {e}")


# Custom exception
class InvalidAgeError(Exception):
    pass


try:
    print(check_age(16))
except InvalidAgeError as e:
    print(f"Error: {e}")

# Chaining exceptions
try:
    num = int("not_a_number")
except ValueError as e:
    raise TypeError("Conversion failed") from e

# Using with for context management
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist!")


# Custom context manager
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}")
        return True  # Suppresses the exception


with MyContextManager():
    print("Inside the context")
    raise ValueError("Something went wrong")
