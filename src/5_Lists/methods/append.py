# The append() method appends an element to the end of the list.

# Syntax
# list.append(elmnt)

# Parameter Values
# Parameter	| Description
# elmnt	    | Required. An element of any type (string, number, object etc.)

# Add an element to the fruits list:
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# Add a list to a list:
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)