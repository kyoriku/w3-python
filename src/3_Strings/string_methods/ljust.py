# The ljust() method will left align the string, using a specified character (space is default) as the fill character.

# Return a 20 characters long, left justified version of the word "banana":
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# Using the letter "O" as the padding character:
txt = "banana"
x = txt.ljust(20, "O")
print(x)