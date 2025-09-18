# The split() method splits a string into a list.

# You can specify the separator, default separator is any whitespace.

# Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

# Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
x = txt.split()
print(x)

# Split the string, using comma, followed by a space, as a separator:
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

# Use a hash character as a separator:
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

# Split the string into a list with max 2 items:
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)