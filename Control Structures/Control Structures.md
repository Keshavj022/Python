# Control Structures

### Control Structures

Control structures are essential in programming as they allow you to control the flow of execution in your code. In Python, control structures include conditional statements and loops, which help you make decisions and repeat actions.

### 1. **Conditional Statements**

Conditional statements enable you to execute specific blocks of code based on certain conditions. Python uses `if`, `elif`, and `else` statements for conditional execution.

**Examples:**

```python
pythonCopy code
# Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# if-elif-else statement
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")

```

**Notes:**

- The `if` statement evaluates a condition, and if it's `True`, the block of code under it executes.
- The `else` statement catches all other cases where the `if` condition is `False`.
- The `elif` (short for else if) allows you to check multiple conditions in sequence.

### 2. **Loops**

Loops are used to execute a block of code multiple times. Python supports two types of loops: `for` and `while`.

### **For Loop**

A `for` loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.

**Examples:**

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for letter in "Python":
    print(letter)

# Using range() with for loop
for i in range(5):
    print(i)  # Outputs numbers from 0 to 4
```

**Notes:**

- The `for` loop iterates over each item in the sequence or iterable.
- The `range()` function generates a sequence of numbers, which is often used in loops.

### **While Loop**

A `while` loop continues to execute as long as a given condition is `True`.

**Examples:**

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Using break to exit a loop
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break  # Exits the loop when count equals 5
```

**Notes:**

- The `while` loop checks the condition before executing the loop's body. If the condition is `True`, it runs the block of code; otherwise, it stops.
- The `break` statement is used to exit the loop prematurely.

### **Break and Continue**

The `break` and `continue` statements provide additional control within loops.

**Examples:**

```python
# Using break to exit a loop early
for i in range(10):
    if i == 5:
        break  # Exits the loop when i is 5
    print(i)

# Using continue to skip the rest of the current iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skips the even numbers
    print(i)
```

**Notes:**

- `break` stops the loop entirely, while `continue` skips the rest of the current iteration and proceeds to the next iteration.

### **List Comprehensions**

List comprehensions provide a concise way to create lists. They are often used to apply an expression to each item in a sequence and collect the results into a new list.

**Examples:**

```python
# Basic list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Outputs: [0, 2, 4, 6, 8]
```

**Notes:**

- List comprehensions are more compact and readable than using traditional loops for generating lists.
- They can include conditions, making them a powerful tool for creating filtered or transformed lists.