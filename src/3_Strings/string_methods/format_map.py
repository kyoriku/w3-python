# The format_map() method formats the specified values of a dictionary and insert them inside the string's placeholders.

# The format_map() method returns the formatted string.

# Insert the name and age from a dictionary into the placeholders.
myvar = {"name" : "Jane", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))