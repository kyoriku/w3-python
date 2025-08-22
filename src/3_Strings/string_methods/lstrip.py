# The lstrip() method removes any leading characters (space is the default leading character to remove)

# Remove spaces to the left of the string:
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

# Remove the leading characters:
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)