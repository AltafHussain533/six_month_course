# In Python, indentation isn't just for readability—it is a requirement of the language.
#  While other languages use curly braces {} to define blocks of code, Python uses whitespace.
# The Basic Concept
# Every time you start a new block of code (like inside an if statement, for loop, or a function),
#  you must indent the following lines. Standard practice is to use 4 spaces per indentation level.
# Coding Examples
# 1. Conditional Statements
# The code inside the if and else blocks must be indented.

# age = 20

# if age >= 18:
#     print("You are an adult.")    # Indented 4 spaces
#     print("Welcome to the club.") # Indented 4 spaces
# else:
#     print("You are a minor.")     # Indented 4 spaces


# age = 20

# if age >= 21:
#     print("You are an adult.")    # Indented 4 spaces
#     print("Welcome to the club.") # Indented 4 spaces
# else:
#     print("You are a minor.")     # Indented 4 spaces

# Critical Rules
# The Colon (:): Every indented block is preceded by a colon.
# Consistency: You cannot mix Tabs and Spaces. Python 3 will throw an IndentationError.
#  Stick to 4 spaces.
# Leveling: If you forget to indent a line that belongs in a block, Python will throw an error; 
# if you indent a line that doesn't belong, the logic will break.
# The "IndentationError"
# If your code looks like this, it will fail:

# if True:
# print("This will cause an IndentationError") # Missing spaces!

# Our Code

# a = 5
# b=15
# c=20.5
# print(a<b)
# if a < b:
#     print("a is less than b")
# print(c<b)
# if c < b:
#     print("c Jo hy woh b sey chotai hy b")
# else:
#     print("c Jo hy woh b sey bara hy b")
