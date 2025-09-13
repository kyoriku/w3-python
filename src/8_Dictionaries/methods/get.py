# The get() method returns the value of the item with the specified key.

# Syntax
# dictionary.get(keyname, value)

# Parameter Values
# Parameter	| Description
# keyname	  | Required. The keyname of the item you want to return the value from
# value	    | Optional. A value to return if the specified key does not exist.
#           | Default value None

# Get the value of the "model" item:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

# Try to return the value of an item that do not exist:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)