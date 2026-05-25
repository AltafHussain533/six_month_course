# Conditional statements
# x = -10
# if x>0:
#     print("x is positive")
# else:
#     print("x is negative")
 
# x=11
# if x>0:
#     print("x is positive")
# elif x<0:
#     print("x is negative")
# else:
#     print("x is zero")

# x=-11
# if x>0:
#     print("x is positive")
# elif x<0:
#     print("x is negative")
# else:
#     print("x is zero")

# for Loops]
# foods = ["dahi Bhallay","Biryani","Samosay","Shami","Palak Paneer"]
# for food in foods:
#     print(food)

# menu = ["dahi Bhallay","Biryani","Samosay","Shami","Palak Paneer"]

# # print(menu[0])
# # print(menu[1])
# print(menu[-5])

# While loop
# i =1 
# while i<6:
#     print(i)
#     i+=1

# i =1 
# while i<100:
#     print(i)
#     i=1 +i   
# for letters in "python":
#     if letters == 'h':
#         break
#     print(letters)

# for letters in "python":
#     if letters == 'h':
#         continue
#     print(letters)

# for letters in "python":
#     if letters == 'h':
#         pass
#     print(letters)

# price = 150

# if price > 200:
#     print("Too expensive")
# elif price > 100:
#     print("Reasonable price") # This will run
# else:
#     print("Cheap!")

# While loop example
# count = 3
# while count > 0:
#     print(count)
#     count -= 1  # Decrease count so the loop eventually ends


for food in ["Biryani", "Samosay", "Shami"]:
    if food == "Samosay":
        continue  # Skip Samosay and move to Shami
    print(f"Serving {food}")
