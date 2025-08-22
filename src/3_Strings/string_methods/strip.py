# The strip() method removes any leading, and trailing whitespaces.

# Leading means at the beginning of the string, trailing means at the end.

# You can specify which character(s) to remove, if not, any whitespaces will be removed.

# Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

# Remove the leading and trailing characters:
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)