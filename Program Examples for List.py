# ----------------------------
# Ex.1.Accessing a single item
# ----------------------------

fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]
last_fruit = fruits[-1]
print("First Fruit:", first_fruit)
print("Last Fruit:", last_fruit)

# -----------------------------------------
# Ex.2.Accessing a range of items (slicing)
# -----------------------------------------

numbers = [10, 20, 30, 40, 50]
subset = numbers[1:4]
print(subset)

# -----------------
# Ex.3.Adding items
# -----------------

fruits = ["apple", "banana", "cherry"]
fruits.append("date") # Adds to the end

# fruits is now ["apple", "banana", "cherry", "date"]

print(fruits)
fruits.insert(1, "avocado") # Inserts at a specific index

# fruits is now ["apple", "avocado", "banana", "cherry", "date"]

print(fruits)

# -------------------
# Ex.4.Removing items
# -------------------

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") # Removes the first occurrence of a value

# fruits is now ["apple", "cherry"]

print(fruits)
removed_item = fruits.pop(0) # Removes and returns the item at a specific index

# removed_item is "apple"; fruits is now ["cherry"]

print(fruits)
del fruits[0] # Deletes the item at a specific index
# fruits is now []

print(fruits)

# -------------------------------
# Ex.5.Modifying an existing item
# -------------------------------

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
# numbers is now [10, 25, 30, 40, 50]

print(numbers)

# -------------------------
# Ex.6.Iterating Over Lists
# -------------------------

colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# Output:
# red
# green
# blue
