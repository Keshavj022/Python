# Importing the math_operations module
import math_operations
# Importing specific functions from the module
from math_operations import add, divide
# Importing a module with an alias
import math_operations as mo
# Importing a function with an alias
from math_operations import subtract as sub
# Importing the math module
import math
# Importing the datetime module
import datetime

# Using the functions from the module
print(math_operations.add(10, 5))
print(math_operations.subtract(10, 5))
print(math_operations.multiply(10, 5))
print(math_operations.divide(10, 0))

# Using the imported functions
print(add(10, 5))
print(divide(10, 2))

# Using the alias to call functions
print(mo.add(10, 5))

print(sub(10, 5))

# Using functions from the math module
print(math.sqrt(16))  # Square root of 16
print(math.pi)  # Value of pi

# Getting the current date and time
current_time = datetime.datetime.now()
print(current_time)
