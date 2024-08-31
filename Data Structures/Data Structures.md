### Data Structures

Data structures are a way of organizing and storing data so that they can be accessed and modified efficiently. Python provides several built-in data structures, each suited for different kinds of operations and use cases. The most commonly used data structures in Python are lists, tuples, dictionaries, and sets.

---

#### 1. **Lists**

A list is an ordered collection of items that can be of any data type. Lists are mutable, meaning you can modify their contents after they have been created.

**Creating a List:**

```python
# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", 3.5, True]
```

**Accessing Elements:**

```python
# Accessing elements by index (0-based)
print(fruits[0])  # Outputs: apple
print(fruits[-1])  # Outputs: cherry (negative index accesses from the end)
```

**Modifying Elements:**

```python
# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # Outputs: ['apple', 'blueberry', 'cherry']
```

**Adding and Removing Elements:**

```python
# Adding elements
fruits.append("orange")  # Adds to the end
fruits.insert(1, "grape")  # Inserts at position 1
print(fruits)  # Outputs: ['apple', 'grape', 'blueberry', 'cherry', 'orange']

# Removing elements
fruits.remove("blueberry")  # Removes the first occurrence of 'blueberry'
popped_fruit = fruits.pop()  # Removes and returns the last item
print(popped_fruit)  # Outputs: orange
```

**Slicing Lists:**

```python
# Slicing
print(fruits[1:3])  # Outputs: ['grape', 'cherry']
print(fruits[:2])  # Outputs: ['apple', 'grape']
print(fruits[2:])  # Outputs: ['cherry']
```

**Iterating Over a List:**

```python
# Iterating over a list
for fruit in fruits:
    print(fruit)
```

---

#### 2. **Tuples**

A tuple is an ordered collection of items that, like a list, can be of any data type. However, tuples are immutable, meaning their contents cannot be changed after they have been created.

**Creating a Tuple:**

```python
# Creating a tuple
coordinates = (10, 20)
single_element_tuple = (5,)  # A comma is required for single-element tuples
```

**Accessing Elements:**

```python
# Accessing elements by index
print(coordinates[0])  # Outputs: 10
```

**Unpacking Tuples:**

```python
# Unpacking tuples
x, y = coordinates
print(x)  # Outputs: 10
print(y)  # Outputs: 20
```

**Using Tuples as Keys in Dictionaries:**

```python
# Tuples can be used as keys in dictionaries
locations = {(10, 20): "A", (30, 40): "B"}
print(locations[(10, 20)])  # Outputs: A
```

---

#### 3. **Dictionaries**

A dictionary is an unordered collection of key-value pairs. Each key must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any data type.

**Creating a Dictionary:**

```python
# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
```

**Accessing Values:**

```python
# Accessing values by key
print(person["name"])  # Outputs: Alice
```

**Modifying Values:**

```python
# Modifying values
person["age"] = 26
print(person)  # Outputs: {'name': 'Alice', 'age': 26, 'city': 'New York'}
```

**Adding and Removing Key-Value Pairs:**

```python
# Adding a new key-value pair
person["email"] = "alice@example.com"
print(person)  # Outputs: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Removing a key-value pair
del person["city"]
print(person)  # Outputs: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
```

**Iterating Over a Dictionary:**

```python
# Iterating over keys
for key in person:
    print(key, person[key])

# Iterating over key-value pairs
for key, value in person.items():
    print(key, value)
```

---

#### 4. **Sets**

A set is an unordered collection of unique items. Sets are useful when you want to eliminate duplicate values or perform set operations like union, intersection, and difference.

**Creating a Set:**

```python
# Creating a set
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 4, 5])  # Creating a set from a list
```

**Adding and Removing Elements:**

```python
# Adding elements
fruits.add("orange")
print(fruits)  # Outputs: {'apple', 'banana', 'cherry', 'orange'}

# Removing elements
fruits.remove("banana")
print(fruits)  # Outputs: {'apple', 'cherry', 'orange'}
```

**Set Operations:**

```python
# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print(a | b)  # Outputs: {1, 2, 3, 4, 5, 6}

# Intersection
print(a & b)  # Outputs: {3, 4}

# Difference
print(a - b)  # Outputs: {1, 2}

# Symmetric Difference
print(a ^ b)  # Outputs: {1, 2, 5, 6}
```

**Checking Membership:**

```python
# Checking membership
print("apple" in fruits)  # Outputs: True
print("banana" in fruits)  # Outputs: False
```

---
You're right! Let's include a detailed section on string manipulation as part of the data structures overview. Strings are a fundamental data type in Python, and mastering string manipulation is essential for effective programming.

---

#### 5. **String Manipulation**

Strings in Python are sequences of characters, making them a very versatile and powerful data type. They are immutable, meaning that once a string is created, it cannot be changed. However, you can create new strings by manipulating the original string.

##### **Creating Strings**

Strings can be created by enclosing characters in single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`) for multi-line strings.

**Examples:**

```python
# Single and double quotes
single_quoted = 'Hello'
double_quoted = "World"

# Triple quotes for multi-line strings
multi_line = """This is a
multi-line string."""
```

##### **String Indexing and Slicing**

You can access individual characters in a string using indexing, and you can extract a portion of a string using slicing.

**Examples:**

```python
# Indexing
word = "Python"
print(word[0])  # Outputs: P
print(word[-1])  # Outputs: n (negative index accesses from the end)

# Slicing
print(word[1:4])  # Outputs: yth (substring from index 1 to 3)
print(word[:2])  # Outputs: Py (substring from the start to index 1)
print(word[3:])  # Outputs: hon (substring from index 3 to the end)
```

##### **String Concatenation and Repetition**

You can concatenate strings using the `+` operator and repeat them using the `*` operator.

**Examples:**

```python
# Concatenation
greeting = "Hello" + " " + "World"
print(greeting)  # Outputs: Hello World

# Repetition
repeat = "Ha" * 3
print(repeat)  # Outputs: HaHaHa
```

##### **String Methods**

Python provides many built-in methods for string manipulation. Here are some of the most commonly used methods:

**Examples:**

```python
# Changing case
text = "Python Programming"
print(text.lower())  # Outputs: python programming
print(text.upper())  # Outputs: PYTHON PROGRAMMING
print(text.title())  # Outputs: Python Programming

# Stripping whitespace
text = "   Hello World   "
print(text.strip())  # Outputs: Hello World
print(text.lstrip())  # Outputs: 'Hello World   '
print(text.rstrip())  # Outputs: '   Hello World'

# Finding and replacing
text = "Hello World"
print(text.find("World"))  # Outputs: 6 (starting index of 'World')
print(text.replace("World", "Python"))  # Outputs: Hello Python

# Splitting and joining
text = "apple,banana,cherry"
fruits = text.split(",")  # Splits the string into a list
print(fruits)  # Outputs: ['apple', 'banana', 'cherry']

new_text = "-".join(fruits)  # Joins the list into a string
print(new_text)  # Outputs: apple-banana-cherry
```

##### **String Formatting**

String formatting allows you to create dynamic strings by embedding expressions within a string. Python provides several ways to format strings, including the `%` operator, the `str.format()` method, and f-strings.

**Examples:**

```python
# Using the % operator
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))  # Outputs: Name: Alice, Age: 30

# Using str.format()
print("Name: {}, Age: {}".format(name, age))  # Outputs: Name: Alice, Age: 30

# Using f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")  # Outputs: Name: Alice, Age: 30
```

##### **String Escaping**

Sometimes you need to include special characters in a string, such as quotes or backslashes. You can escape these characters using the backslash `\`.

**Examples:**

```python
# Escaping quotes
quote = 'She said, "Hello!"'
print(quote)  # Outputs: She said, "Hello!"

# Escaping backslashes
path = "C:\\Users\\Alice\\Documents"
print(path)  # Outputs: C:\Users\Alice\Documents
```

##### **Checking String Properties**

You can check various properties of strings, such as whether they contain only digits, are alphabetic, or are alphanumeric.

**Examples:**

```python
# Checking properties
text = "Python123"
print(text.isalpha())  # Outputs: False (contains digits)
print(text.isdigit())  # Outputs: False (contains letters)
print(text.isalnum())  # Outputs: True (contains only letters and digits)
```

---

This section provides a comprehensive overview of Python's built-in data structures, complete with explanations and code examples to help you understand and utilize these structures effectively.