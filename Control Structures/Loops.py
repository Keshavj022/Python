# For Loop

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
