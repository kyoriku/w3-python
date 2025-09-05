# The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
# You can specify as many sets you want, separated by commas.
# It does not have to be a set, it can be any iterable object.
# If an item is present in more than one set, the result will contain only one appearance of this item.
# As a shortcut, you can use the | operator instead, see example below.

# Syntax
# set.union(set1, set2...)

# Parameter Values
# Parameter	| Description
# set1	    | Required. The iterable to unify with
# set2	    | Optional. The other iterable to unify with.
#           | You can compare as many iterables as you like.
#           | Separate each iterable with a comma

# Shorter Syntax
# set | set1 | set2 ...

# Parameter Values
# Parameter	| Description
# set1	    | Required. The iterable to unify with
# set2	    | Optional. The other iterable to unify with.
#           | You can compare as many iterables as you like.
#           | Separate each iterable with | (a pipe operator).
#           | See examples below.

# Return a set that contains all items from both sets, duplicates are excluded:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

# Use | as a shortcut instead of union():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x | y
print(z)

# Unify more than 2 sets:
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)

# Unify 3 sets with the | operator:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x | y | z
print(result)