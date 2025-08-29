# The extend() method adds the specified list elements (or any iterable) to the end of the current list.

# Syntax
# list.extend(iterable)

# Parameter Values
# Parameter	| Description
# iterable	| Required. Any iterable (list, set, tuple, etc.)

# Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# Add a tuple to the fruits list:
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)
