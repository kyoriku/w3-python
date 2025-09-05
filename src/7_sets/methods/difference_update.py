# The difference_update() method removes the items that exist in both sets.
# The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
# As a shortcut, you can use the -= operator instead, see example below.

# Syntax
# set.difference_update(set1, set2 ... etc.)

# Parameter Values
# Parameter	| Description
# set1	    | Required. The set(s) to check for differences in.
# set2	    | Optional. The other set to search for equal items in.
#           | You can compare as many sets you like.
#           | Separate the sets with a comma.
#           | See examples below.

# Shorter Syntax
# set -= set1 | set2 ... etc.

# Parameter Values
# Parameter	| Description
# set1	    | Required. The set(s) to check for differences in.
# set2	    | Optional. The other set to search for equal items in.
#           | You can compare as many sets you like.
#           | Separate the sets with | (a pipe operator).
#           | See examples below.

# Remove the items that exist in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

# Use -= as a shortcut instead of difference_update():
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
a -= b
print(a)

# Join more than two sets:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
a.difference_update(b, c)
print(a)

# Join more than two sets with the -= operator:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
a -= b | c
print(a)