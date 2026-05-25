# print("We are learning python with codanics")  # String

# 1. Arithmetic & Assignment
# Arithmetic operators perform calculations, while assignment operators update variable values efficiently
# a, b = 10, 3
# print(a + b)   # 13 (Addition)
# print(a // b)  # 3  (Floor Division - drops decimal)
# print(a % b)   # 1  (Modulus - remainder)

# c = 5
# c += 2         # Same as c = c + 2
# print(c)       # 7

# 2. Concatenation & Repetition
# The + operator joins strings together, while the * operator repeats a string a specific number of times. 
# Join two strings
# first = "Hello"
# second = "World"
# print(first + " " + second)  # Output: Hello World

# # Repeat a string
# greet = "Hi! "
# print(greet * 3)             # Output: Hi! Hi! Hi! 

# 3. Membership Operators
# The in and not in operators check if a specific substring exists within a larger string. 
# text = "Python Programming"

# print("Python" in text)      # Output: True
# print("Java" not in text)    # Output: True
# print("Java"  in text)    # Output: False

# 4. Comparison & Logical
# These are used in conditional logic to return 

# print(10 > 3)        # True
# print(10 == 3)       # False (Checks equality)

# # x, y = True, False
# # print(x and y)       # False (Both must be true)
# # print(not x)         # False (Inverts result)


# # 5. Membership & Identity
# # These operators check for the presence of items in a collection or verify if two variables refer 
# # to the same object in memory.

# fruits = ["apple", "banana"]
# print("apple" in fruits) # True

# list1 = [1, 2]
# list2 = [1, 2]
# list3 = list1
# print(list1 is list2)    # False (Different objects with same content)
# print(list1 is list3)    # True (Same object in memory)


# my code

print('codanics') # String
print("Ammar")    # String
print('''Aammar codanics''')  # String
print(2+3)    # Integer
print(3.5-2.1)   # Float
print(10 * 5)    # Integer
a=[1,2,3]
b=[4,5,6]
c=[4,5,6]
print(a)
print(b)
print(a+b)
print(a==b)
print(b==c)
