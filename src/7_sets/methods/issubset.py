# The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
# As a shortcut, you can use the <= operator instead, see example below.

# Syntax
# set.issubset(set1)

# Shorter Syntax
# set <= set1

# Parameter Values
# Parameter	| Description
# set1	    | Required. The set to search for equal items in

# Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# Use <= as a shortcut instead of issubset():
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x <= y
print(z)

# What if not all items are present in the specified set?
# Return False if not all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)

# Python Set < (less than) Method
# The < returns True if all items in the set exists in a specified larger set, otherwise it returns False.

# Syntax
# set1 < set2

# Returns False even if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"c", "b", "a"}
z = x < y
print(z)

# Returns True because all items of set x is present in the larger set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x < y
print(z)