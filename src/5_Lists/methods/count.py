# The count() method returns the number of elements with the specified value.

# Syntax
# list.count(value)

# Parameter Values
# Parameter	| Description
# value	    | Required. Any type (string, number, list, tuple, etc.). The value to search for.

# Return the number of times the value "cherry" appears in the fruits list:
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

# Return the number of times the value 9 appears in the list:
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)