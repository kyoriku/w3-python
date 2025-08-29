# The pop() method removes the element at the specified position.

# Syntax
# list.pop(pos)

# Parameter Values
# Parameter	| Description
# pos	      | Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item

# Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# Return the removed element:
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)

# Note: The pop() method returns removed value.