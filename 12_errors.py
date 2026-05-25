# Syntax or Indentation Error
# x =5
# if x > 3:
# print("x is positive value")   

# # logical or human error
# if x > 3:
#     print("y is positive value")

# # runtime or module not found error
# import numpy as np
# print(np.sqrt(36))

# 1. SyntaxError
# Occurs when the code violates Python's structural rules (checked before the code runs)
# Missing a colon at the end of the if statement
if True
    print("Hello")

# 2. NameError
# Occurs when you try to use a variable or function that hasn't been defined
# 'total' hasn't been created yet

print(total)


# 3. TypeError
# Occurs when an operation is applied to an object of an inappropriate type
# You cannot add a string to an integer
result = Age:  + 25


# 4. ValueError
# Occurs when a function receives an argument of the right type but an inappropriate value
# 'abc' is a string (right type), but cannot be converted to an integer
number = int("abc")


# 5. IndexError
# Occurs when you try to access an index that is out of range for a list or other sequence
# The list only has 3 items (indices 0, 1, 2)
items = [10, 20, 30]
print(items[5])

# 6. KeyError
# Occurs when you try to access a key that doesn't exist in a dictionary

user = {"name": "Alice"}
# 'email' is not a key in this dictionary
print(user["email"])


# 7. AttributeError
# Occurs when you try to call a method or attribute that an object doesn't have
number = 10
# Integers do not have an .append() method
number.append(5)

# 8. ImportError
# Occurs when an import statement fails to find the module or one of its components   
# Trying to import a library that isn't installed
import nonexistent_library

# 9. ZeroDivisionError
# Occurs when you try to divide a number by zero
result = 100 / 0

# 10. FileNotFoundError
# Occurs when you try to open a file that doesn't exist
with open("ghost_file.txt", "r") as f:
    data = f.read()
# 16. MemoryError
# Occurs when an operation runs out of memory, such as trying to create a very large list or array
# Attempting to create a list so large it crashes the memory
huge_list = [1] * (10**12)

# timeout error
# Occurs when a process takes too long to complete, often in network operations or long-running computations
import socket

# Attempting to connect to a non-responsive address with a short timeout
s = socket.socket()
s.settimeout(0.01)
s.connect(("192.168.1.254", 80))


