# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False.
# As a shortcut, you can use the >= operator instead, see example below.

# Syntax
# set.issuperset(set)

# Shorter Syntax
# set >= set1

# Parameter Values
# Parameter	| Description
# set	      | Required. The set to search for equal items in

# Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

# Use >= as a shortcut instead of issuperset():
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x >= y
print(z)

# What if not all items are present in the specified set?
# Return False if not all items in set y are present in set x:
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

# Python Set > (greater than) Method
# The > returns True if all items of a specified smaller set exists in the current set, otherwise it returns False.

# Syntax
# set1 > set2

# Returns False even if all items in set y are present in set x:
x = {"a", "b", "c"}
y = {"c", "b", "a"}
z = x > y
print(z)

# Returns True because all items of the smaller set y is present in the set x:
x = {"a", "b", "c"}
y = {"b", "a"}
z = x > y
print(z)