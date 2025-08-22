# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

# Example of characters that are not alphanumeric: (space)!#%&? etc.

# Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)

# Check if all the characters in the text is alphanumeric:
txt = "Company 12"
x = txt.isalnum()
print(x)