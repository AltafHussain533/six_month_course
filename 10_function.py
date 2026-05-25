# def greet_user():
#     print("Hello, user!")
# greet_user()  # Calling the function to execute its code

# def aoa():
#     print("Assalamu Alaikum, All the way from london")
# aoa()  # Calling the function to execute its code

# def aoa(name):
#     print(f"Assalamu Alaikum, {name}!") 
# aoa("Ali")  # Calling the function with an argument to execute its code

# def aoa(name):
#     print(f"Assalamu Alaikum, {name}!, Kaifa haluk?") 
# aoa("Ali")  # Calling the function with an argument to execute its code

# def aoa(name="khuda kay banday"):
#     print(f"Assalamu Alaikum, {name}!, Kaifa haluk?")
# aoa()  # Calling the function without an argument to use the default value

# def aoa(name="Merayt Payaray Bhai"):
#     print(f"Assalamu Alaikum, {name}!, Kaifa haluk?")
# aoa("Azam")  # Calling the function with an argument to execute its code

# def aoa(name="Merayt Payaray Bhai"):
#     print(f"Assalamu Alaikum, {name}!, Kaifa haluk?")
# aoa()  # Calling the function with an argument to execute its code

# # Return Values
# def square(number):
#     return number *number
# square(9)  # Calling the function to execute its code and return the result    no result appear

# # Return Values   Error
# def square(number+1):
#     return number *number
# print(square(9))  # Calling the function to execute its code and return the result

# # Return Values   
# def square(number):
#     return number *number
# result = square(9)  # Calling the function to execute its code and return the result
# print(result)  # Printing the result returned by the function

# # Recursion
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(6))  # Calling the function to execute its code and return the result

# # Lambda Function
# x = lambda a: a + 10
# print(x(5))  # Calling the lambda function to execute its code and return the result

# x = lambda a: a/2
# print(x(4))  # Calling the lambda function to execute its code and return the result

# x = lambda a, b: a * b
# print(x(5, 6))  # Calling the lambda function to execute its code and return the result

# def x(a):
#     return a / 2
# x = lambda a: a / 2
# print(x(4))  # Calling the lambda function to execute its code and return the result

# def x(a, b):
#     return a * b
# x = lambda a, b: a * b
# print(x(2, 8))  # Calling the lambda function to execute its code and return the result


# Internet function
# 1. Basic Function with Arguments
# This function takes two numbers and returns their sum

# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 10)
# print(result) # Output: 15


# 2. Function with Default Parameters
# You can set a default value for a parameter. If the caller doesn't provide one, the default is used.
# def greet(name="Guest"):
#     return f"Hello, {name}!"
# print(greet()) # Output: Hello, Guest!
# print(greet("Alice")) # Output: Hello, Alice!


# 3. Recursive Function
# A function that calls itself to solve a problem. This is often used for tasks like calculating factorials or traversing data structures.
# def factorial(n): 
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5)) # Output: 120

# 4. Lambda Function
# A small anonymous function defined with the lambda keyword. It can take any number of arguments but can only have one expression.
# square = lambda x: x * x
# print(square(4)) # Output: 16 

# ten functions define krna hai k kay sat aur lambda kay sat

# 1. Basic Multiplier
# Uses a default keyword k to multiply an input x.
mult = lambda x, k=2: x * k
print(mult(5))          # Output: 10 (uses default k=2)
print(mult(5, k=10))    # Output: 50


# 2. Power Function
# Raises a number to a specified power, with a default of 2 (squaring)
power = lambda x, p=2: x ** p
print(power(3))         # Output: 9 (3 squared)
print(power(3, p=3))   # Output: 27 (3 cubed)

# 3. String Repeater
# Repeats a string a specified number of times, with a default of 3.
repeat = lambda s, n=3: s * n
print(repeat("Hi "))    # Output: "Hi Hi Hi "
print(repeat("Hi ", n=5))  # Output: "Hi Hi Hi Hi Hi "

# 4. Area of Circle
# Calculates the area of a circle given its radius, with a default value of 1.
area_circle = lambda r, pi=3.14: pi * (r ** 2)
print(area_circle(5))   # Output: 78.5 (area of circle with
# radius 5)
print(area_circle(5, pi=3.14159))  # Output: 78.53975 (using more precise pi)

# 5. Temperature Converter
# Converts Celsius to Fahrenheit, with a default of 0°C.
c_to_f = lambda c, offset=32: (c * 9/5) + offset
print(c_to_f(0))        # Output: 32.0 (freezing point of water)
print(c_to_f(100))      # Output: 212.0 (boiling point of water)    

# 6. List Multiplier
# Multiplies each element in a list by a specified factor, with a default of 2.
list_mult = lambda lst, factor=2: [x * factor for x in lst]     
print(list_mult([1, 2, 3]))          # Output: [2, 4, 6]
print(list_mult([1, 2, 3], factor=3))  # Output: [3, 6, 9]  

# 7. String Length Checker
# Checks if the length of a string is greater than a specified threshold, with a default of 5.
length_check = lambda s, threshold=5: len(s) > threshold        
print(length_check("Hello"))       # Output: False (length is 5)
print(length_check("Hello, World!"))  # Output: True (length is 13) 
# 8. Discount Calculator
# Calculates the discounted price given an original price and a discount percentage, with a default discount of 10%.
discount = lambda price, percent=10: price * (1 - percent / 100)    
print(discount(100))          # Output: 90.0 (10% discount)
print(discount(100, percent=20))  # Output: 80.0 (20% discount) 

# 9. Even or Odd Checker
# Determines if a number is even or odd, with a default of 0 (which is even).
even_odd = lambda n, default=0: "Even" if n % 2 == 0 else "Odd"
print(even_odd(0))           # Output: "Even" (default value)           
print(even_odd(7))           # Output: "Odd" (7 is odd)
print(even_odd(10))          # Output: "Even" (10 is even)      

# 10. Maximum of Two Numbers
# Returns the maximum of two numbers, with a default of 0 for both.     
max_num = lambda a=0, b=0: a if a > b else b
print(max_num())             # Output: 0 (both defaults)    
print(max_num(5))            # Output: 5 (b is default 0)
print(max_num(5, 10))        # Output: 10 (10 is greater than 5)    
    