# Basic list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Outputs: [0, 2, 4, 6, 8]
