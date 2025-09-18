# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

# Remove any white spaces at the end of the string:
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

# Remove the trailing characters if they are commas, periods, s, q, or w:
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)