# The add() method adds an element to the set.
# If the element already exists, the add() method does not add the element.

# Syntax
# set.add(elmnt)

# Parameter Values
# Parameter	| Description
# elmnt	  | Required. The element to add to the set

# Add an element to the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# Try to add an element that already exists:
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)