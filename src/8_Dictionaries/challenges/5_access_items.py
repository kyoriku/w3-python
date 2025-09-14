# Access dictionary keys and add a key-value pair.

# Requirements
# x holds the initial keys
# The car dictionary contains the new 'color' key, with value 'white'.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Create a variable x storing the keys of the car dictionary
x = car.keys()

print(x) # before the change

# Add a new key-value pair 'color' : 'white'
car['color'] = 'white'

print(x) # after the change