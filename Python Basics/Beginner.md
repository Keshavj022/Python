# Beginner

### 1. **Print Statement**

The `print()` function is one of the most commonly used functions in Python. It outputs data to the console.

**Examples:**

```python
# Printing Hello World
print("Hello World")

# Printing multiple lines using new line character
print("Hello World\nHello World\nHello World")

# Concatenating Strings
print("Hello" + " Python")

# Adding space while concatenating
print("Hello " + "Python")

# Using formatted strings
name = "User"
print(f"Your name is {name}")
```

**Notes:**

- The `\n` character is used to create a new line in the output.
- Using `+` between strings concatenates them directly.
- Formatted strings (f-strings) allow embedding expressions inside string literals, prefixed by `f`.

---

### 2. **Variables**

Variables in Python are used to store data values. A variable is created the moment you first assign a value to it.

**Examples:**

```python
# String Variable
name = "User"
print(name)
print(type(name))  # Checking the type of the variable
print(len(name))   # Length of the string

# Integer Variable
number = 1234
print(number)
print(type(number))  # Type will be int

# Float Variable
number3 = 90.233
print(type(number3))  # Type will be float

# Adding Two Integers
number1 = 34
number2 = 35
sum_int = number1 + number2
print(sum_int)

# Adding Two Float Numbers
number4 = 30.5
number5 = 21.8
sum_float = number4 + number5
print(sum_float)
```

**Notes:**

- Variables do not need explicit declaration before using them.
- Python is dynamically typed, meaning the variable type is determined at runtime based on the value assigned.

---

### 3. **Data Types**

Python supports several built-in data types, such as integers, floats, strings, and booleans.

**Examples:**

```python
# Subscripting in Strings
print("Hello"[0])  # Outputs: H
print("Hello"[-1]) # Outputs: o
print("Hello"[4])  # Outputs: o
print("1234" + "5678")  # Concatenating strings

# Integers
print(1233445)

# Large Integers (underscore for readability)
print(123_456_789)

# Float
print(123.89)

# Boolean
print(True)
print(False)
```

**Notes:**

- Subscripting allows accessing individual characters in a string.
- Python supports underscores in numeric literals to improve readability.

---

### 4. **Taking Input**

You can take user input using the `input()` function.

**Examples:**

```python
# Taking input from the user
input("Enter your name")

# Using input directly in a print statement
print("Hello " + input("Enter your name"))

# Storing input in a variable and displaying it
name = input("Enter your name")
print("Your name is " + name)
```

**Notes:**

- The `input()` function always returns data as a string. If you need a different type, you should explicitly convert it.

---

### 5. **Mathematical Operations**

Python supports various mathematical operations, including addition, subtraction, division, multiplication, and exponentiation.

**Examples:**

```python
print(123 + 456)  # Addition
print(7 - 3)      # Subtraction
print(6 / 3)      # Division (always returns a float)
print(6 // 2)     # Floor division (returns an integer)
print(2 ** 2)     # Exponentiation

# PEMDAS Order
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(int(4555.45))  # Converts float to integer
print(round(3234.6))  # Rounds to nearest integer
print(round(455.44332, 2))  # Rounds to 2 decimal places

# Incrementing a variable
a = 1
print(a)
a += 1
print(a)
```

**Notes:**

- The order of operations in Python follows PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).
- Use `int()` for converting float to integer and `round()` for rounding off numbers.