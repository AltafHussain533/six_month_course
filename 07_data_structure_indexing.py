# Data structures in Python are specialized formats for organizing and storing data 
# in computer memory to enable efficient access and modification.
# They are broadly categorized into built-in and user-defined structures. 

# 1. Built-in Data Structures
# These are natively supported by Python and available without importing extra modules. 

# Lists ([]): Ordered and mutable collections that allow duplicate elements. 
# They are ideal for storing sequences of related items where modification is needed.
# Tuples (()): Ordered but immutable collections. Once created, they cannot be changed, 
# making them more memory-efficient and safer for fixed data like coordinates.
# Dictionaries ({key: value}): Unordered (pre-3.7) or ordered (3.7+) collections of key-value pairs.
# They provide extremely fast O(1) lookups by using a hash table implementation.
# Sets ({}): Unordered collections of unique elements. 
# They are highly optimized for membership testing and mathematical operations like union and intersection. 

# 2. Specialized Standard Library Structures
# The collections module provides enhanced containers for specific tasks: 

# Deque: A double-ended queue designed for fast appends and pops from both ends.
# NamedTuple: Assigns names to each position in a tuple for more readable code.
# Counter: A dictionary subclass for counting hashable objects.
# defaultdict: A dictionary that provides a default value for missing keys. 

# 3. User-Defined Data Structures
# These are advanced structures implemented using Python classes to solve specific computational problems. 
# Stack: Follows LIFO (Last-In-First-Out) logic, where the last item added is the first one removed.

# Queue: Follows FIFO (First-In-First-Out) logic, similar to a real-life waiting line.
# Linked List: A linear structure where elements (nodes) are not stored contiguously but linked via pointers.
# Tree: A hierarchical structure with a "root" node and "child" nodes, 
# often used in searching and file systems.
# Graph: A collection of nodes (vertices) connected by edges, used to model networks like social connections. 

# 4. Third-Party Library Structures
# For large-scale data science and numerical work, external libraries offer highly optimized structures: 

# NumPy Arrays: More memory-efficient than lists for massive numerical datasets.
# Pandas DataFrames: A tabular structure (like a spreadsheet) that can store mixed data types in labeled columns. 


# food =["Dahi Bhallay", "Biryani", "Samosay", "Shami", "Palak Paneer"]
# print(food)  # Output: ['Dahi Bhallay', 'Biryani', 'Samosay', 'Shami', 'Palak Paneer']  
# print(food[0])  # Output: Dahi Bhallay
# print(food[1])  # Output: Biryani
# print(food[2])  # Output: Samosay
# print(food[3])  # Output: Shami
# print(food[4])  # Output: Palak Paneer  
# print(food[-1])  # Output: Palak Paneer
# print(food[-2])  # Output: Shami        
# print(food[0:3])  # Output: ['Dahi Bhallay', 'Biryani', 'Samosay']
# print(food[2:])  # Output: ['Samosay', 'Shami', 'Palak Paneer']
# print(food[:3])  # Output: ['Dahi Bhallay', 'Biryani', 'Samosay']
# print(food[::2])  # Output: ['Dahi Bhallay', 'Samosay', 'Palak Paneer']
# print(food[::-1])  # Output: ['Palak Paneer', 'Shami', 'Samosay', 'Biryani', 'Dahi Bhallay']    
# print(food[1:4:2])  # Output: ['Biryani', 'Shami']
# print(food[0:5:3])  # Output: ['Dahi Bhallay', 'Shami']
# print(food[-7])
# 2_Tuples

# coordinates = (4.21, 9.29)
# print(coordinates)  # Output: (4.21, 9.29)
# print(coordinates[0])  # Output: 4.21
# print(coordinates[1])  # Output: 9.29
# print(coordinates[-1])  # Output: 9.29
# print(coordinates[-2])  # Output: 4.21
# print(coordinates[0:2])  # Output: (4.21, 9
 # 3_set
# fruit_set ={"Dahi Bhallay", "Biryani", "Samosay", "Shami", "Palak Paneer"}
# print(fruit_set)  # Output: {'Dahi Bhallay', 'Biryani', 'Samosay', 'Shami', 'Palak Paneer'}
# fruit_set.add("Pakora")
# print(fruit_set)  # Output: {'Dahi Bhallay', 'Biryani', 'Samosay', 'Shami', 'Palak Paneer', 'Pakora'}

# 4_Dictionary
# person = {"name": "Ali", "age": 30, "city": "Karachi"}
# print(person)  # Output: {'name': 'Ali', 'age': 30, 'city': 'Karachi'}
# print(person["name"])  # Output: Ali
# print(person["age"])  # Output: 30
# print(person["city"])  # Output: Karachi


car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(car)  # Output: {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020}
print(car["brand"])  # Output: Toyota
print(car["model"])  # Output: Corolla
print(car["year"])  # Output: 2020
