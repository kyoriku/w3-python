# Get the dictionary items, and add a key-value pair to the dictionary.

# Requirements
# The car dictionary should initially contain the keys 'brand', 'model', and 'year'.
# The variable x should include the key 'color' after its addition to the dictionary.
# The 'color' key in the car dictionary should have the value 'red'.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Complete the code line to get the dictionary items, and store them in variable x
x = car.items()

print(x)

# Add a new key "color", with value "red"
car["color"] = "red"

print(x)