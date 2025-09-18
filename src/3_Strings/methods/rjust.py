# The rjust() method will right align the string, using a specified character (space is default) as the fill character.

# Return a 20 characters long, right justified version of the word "banana":
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
# Note: In the result, there are actually 14 whitespaces to the left of the word banana.

# Using the letter "O" as the padding character:
txt = "banana"
x = txt.rjust(20, "O")
print(x)