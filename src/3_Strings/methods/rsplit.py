# The rsplit() method splits a string into a list, starting from the right.

# If no "max" is specified, this method will return the same as the split() method.

# Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

# Split a string into a list, using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

# Split the string into a list with maximum 2 items:
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)