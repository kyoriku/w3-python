# The index() method returns the position at the first occurrence of the specified value.

# Syntax
# list.index(elmnt, start, end)

# Parameter Values
# Parameter	| Description
# elmnt	    | Required. Any type (string, number, list, etc.). The element to search for
# start	    | Optional. A number representing where to start the search
# end	      | Optional. A number representing where to end the search

# What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# What is the position of the value 32:
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

# Find the position of 'cherry', but start the search at position 4:
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index("cherry", 4)
print(x)

# Note: The index() method only returns the first occurrence of the value.