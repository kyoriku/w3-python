# The update() method updates the current set, by adding items from another set (or any other iterable).

# If an item is present in both sets, only one appearance of this item will be present in the updated set.

# As a shortcut, you can use the |= operator instead, see example below.

# Syntax
# set.update(set1, set2 ...)

# Parameter Values
# Parameter	| Description
# set1	    | Required. The iterable insert into the current set
# set2	    | Optional. More iterables to insert into the current set.
#           | You can insert as many iterables as you like.
#           | Separate each iterable with a comma.

# Shorter Syntax
# set |= set1 | set2 ...

# Parameter Values
# Parameter	| Description
# set1	    | Required. The set to insert into the current set.
# set2	    | Optional. More sets to insert into the current set.
#           | You can insert as many sets you like.
#           | Separate the sets with | (pipe operator).
#           | See examples below.

# Insert the items from set y into set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

# Use |= as a shortcut instead of update():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x |= y
print(x)

# Insert more than one set:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x.update(y, z)
print(x)

# Join more than one set with the |= operator:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x |= y | z
print(x)