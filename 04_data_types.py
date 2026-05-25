#

# Assigment: difference between set and list

# The primary difference between a list and a set is how they handle order and duplicate items. 
# A list is an ordered collection that allows multiple identical entries,
# whereas a set is an unordered collection that only stores unique elements. 


# Key Differences at a Glance

# Feature 	              List	                      
	
 # Duplicates          # Does not allow duplicates; all elements must be unique.
# Ordering	           Maintains the order in which items are inserted (insertion order).	
# Access	           Elements can be accessed by their index/position.	
# Performance	        Slower for searching/membership tests as it may check every item.	
# Common Syntax		    Often defined with curly braces {} in Python or HashSet in Java.	

 # Feature                  #Set

# Duplicates	       Allows duplicate elements.
# Ordering             Does not maintain any specific order.
# Access               No index-based access; items are usually checked for membership.
# Performance      	   Extremely fast for membership tests due to internal "hashing".
# Common Syntax	    	Defined with curly braces {} in Python or HashSet in Java.


# When to Use Which?
# Use a List when you care about the order of your data (like a history log or a task queue) or if you specifically need to keep track of repeating items.
# Use a Set when you need to ensure uniqueness (like a list of user IDs or unique visitors) or when you need to perform fast lookups to check if an item exists. 

# Examples
# List Example: A grocery list where you might have "Apples" written twice if you need two bags.
# Set Example: A collection of unique guest IDs for a party; if someone is added twice, the set will still only list them once

# Numeric types
age = 25              # int
price = 19.99         # float
coordinates = 3 + 5j  # complex

# Text and Boolean
name = "Alice"        # str
is_active = True      # bool

# Collections (Sequences, Mappings, Sets)
fruits = ["apple", "banana"]        # list (mutable)
point = (10, 20)                    # tuple (immutable)
user = {"id": 1, "name": "Alice"}   # dict
unique_ids = {101, 102, 103}        # set

# A list containing only integers
numbers = [10, 20, 30, 40, 50]

# Accessing the first element
print(numbers[0])  # Output: 10

# Adding a new number
numbers.append(60)
print(numbers)     # Output: [10, 20, 30, 40, 50, 60]
# A tuple containing a mix of data types
person = ("Alice", 30, "Engineer")
print(person)      # Output: ("Alice", 30, "Engineer")

# A list containing only strings
fruits = ["apple", "banana", "cherry"]

# Accessing the last element
print(fruits[-1])  # Output: cherry

# Modifying an element
fruits[1] = "blueberry"
print(fruits)      # Output: ['apple', 'blueberry', 'cherry']


