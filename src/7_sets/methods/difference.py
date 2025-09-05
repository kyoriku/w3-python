# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.
# As a shortcut, you can use the - operator instead, see example below.

# Syntax
# set.difference(set1, set2 ... etc.)

# Parameter Values
# Parameter	| Description
# set1    	| Required. The set(s) to check for differences in.
# set2	    | Optional. The other set to search for equal items in.
#           | You can compare as many sets you like.
#           | Separate the sets with a comma.
#           | See examples below.

# Shorter Syntax
# set - set1 - set2 .... etc.

# Parameter Values
# Parameter	| Description
# set1	    | Required. The set(s) to check for differences in.
# set2	    | Optional. The other set to search for equal items in.
#           | You can compare as many sets you like.
#           | Separate the sets with - (a minus operator).
#           | See examples below.

# Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

# Use - as a shortcut instead of difference():
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
myset = a - b
print(myset)

# Join more than two sets:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
myset = a.difference(b, c)
print(myset)

# Join more than two sets with the - operator:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
myset = a - b - c
print(myset)

# Reverse the example on the top of this page. Return a set that contains the items that only exist in set y, and not in set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)