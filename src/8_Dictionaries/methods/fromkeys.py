# The fromkeys() method returns a dictionary with the specified keys and the specified value.

# Syntax
# dict.fromkeys(keys, value)

# Parameter Values
# Parameter	| Description
# keys	    | Required. An iterable specifying the keys of the new dictionary
# value	    | Optional. The value for all keys. Default value is None

# Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

# Same example as above, but without specifying the value:
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)