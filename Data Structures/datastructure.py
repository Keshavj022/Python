# List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Outputs: ['apple', 'banana', 'cherry', 'orange']
fruits.remove("banana")
print(fruits)  # Outputs: ['apple', 'cherry', 'orange']

# Tuple
coordinates = (10, 20)
x, y = coordinates
print(x, y)  # Outputs: 10 20

# Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
person["age"] = 26
person["email"] = "alice@example.com"
del person["city"]
print(person)  # Outputs: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

# Set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection: {3, 4}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric Difference: {1, 2, 5, 6}


# String Manipulation
# Creation
single_quoted = 'Hello'
double_quoted = "World"
multi_line = """This is a
multi-line string."""

# Indexing and slicing
word = "Python"
print(word[0])  # Outputs: P
print(word[-1])  # Outputs: n
print(word[1:4])  # Outputs: yth

# Concatenation and repetition
greeting = "Hello" + " " + "World"
repeat = "Ha" * 3
print(greeting)  # Outputs: Hello World
print(repeat)  # Outputs: HaHaHa

# String methods
text = "Python Programming"
print(text.lower())  # Outputs: python programming
print(text.strip())  # Outputs: Python Programming
print(text.replace("Programming", "Language"))  # Outputs: Python Language

# Splitting and joining
fruits = "apple,banana,cherry".split(",")
print(fruits)  # Outputs: ['apple', 'banana', 'cherry']
print("-".join(fruits))  # Outputs: apple-banana-cherry

# String formatting
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")  # Outputs: Name: Alice, Age: 30

# String escaping
quote = 'She said, "Hello!"'
path = "C:\\Users\\Alice\\Documents"
print(quote)  # Outputs: She said, "Hello!"
print(path)  # Outputs: C:\Users\Alice\Documents

# Checking string properties
text = "Python123"
print(text.isalpha())  # Outputs: False
print(text.isdigit())  # Outputs: False
print(text.isalnum())  # Outputs: True
