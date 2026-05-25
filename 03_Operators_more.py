x=15
y = 4
z = 5.5
print(x + y)  # Addition: 19
print(x - y)  # Subtraction: 11 
print(x * y)  # Multiplication: 60
a="codanics"
b="Pakistan"
print(a)
a = "We are learning coding with Python at codanics"
print(a+b)
print(x - y)  # Subtraction: 11 
print(x - z)  # Subtraction: 9.5
print(x * y)  # Multiplication: 60
print(x * z)  # Multiplication: 82.5
print(x / y)  # Division: 3.75  
print(x / z)  # Division: 2.727272727272727
print(x // y) # Floor Division: 3
print(x // z) # Floor Division: 2   
print(x - z *4/y + 3) # Mixed Operators: 15 - (5.5 * 4 / 4) + 3 = 15 - 5.5 + 3 = 12.5

# DMAS
# PEMDAS
# BODAS

# # How DMAS Works in Python
# # In an expression with multiple operators, Python executes them in this specific order: 
# # Division (/) and Multiplication (*) — Same priority (left-to-right).
# # Addition (+) and Subtraction (-) — Same priority (left-to-right).
# # Expression: 10 + 5 * 4 / 2 - 3

# # Step-by-step logic:
# # 1. 4 / 2 = 2.0 (Division)
# # 2. 5 * 2.0 = 10.0 (Multiplication)
# # 3. 10 + 10.0 = 20.0 (Addition)
# # 4. 20.0 - 3 = 17.0 (Subtraction)

# result = 10 + 5 * 4 / 2 - 3
# print(f"The result is: {result}") # Output: 17.0

# # The PEMDAS Order
# # Parentheses ()
# # Exponents **
# # Multiplication * and Division /, //, % (Left-to-right)
# # Addition + and Subtraction - (Left-to-right)

# # Expression: 5 + (10 - 2) ** 2 / 4 * 2

# # Step-by-step evaluation:
# # 1. (10 - 2) = 8            <- Parentheses
# # 2. 8 ** 2 = 64             <- Exponent
# # 3. 64 / 4 = 16.0           <- Division (left-to-right)
# # 4. 16.0 * 2 = 32.0         <- Multiplication (left-to-right)
# # 5. 5 + 32.0 = 37.0         <- Addition

# result = 5 + (10 - 2) ** 2 / 4 * 2
# print(result)  # Output: 37.0


# # Expression: 10 + (2 * 3) ** 2 / 4 - 5

# # Step-by-step logic:
# # 1. (2 * 3) = 6             <- Brackets (B)
# # 2. 6 ** 2 = 36             <- Orders/Exponents (O)
# # 3. 36 / 4 = 9.0            <- Multiplication/Division (M/D)
# # 4. 10 + 9.0 = 19.0         <- Addition/Subtraction (A/S)
# # 5. 19.0 - 5 = 14.0         <- Final result

# result = 10 + (2 * 3) ** 2 / 4 - 5
# print(f"The final result is: {result}") # Output: 14.0
