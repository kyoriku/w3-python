# The isprintable() method returns True if all the characters are printable, otherwise False.

# Example of none printable character can be carriage return and line feed.

# Check if all the characters in the text are printable:
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

# Check if all the characters in the text are printable:
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)