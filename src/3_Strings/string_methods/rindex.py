# The rindex() method finds the last occurrence of the specified value.

# The rindex() method raises an exception if the value is not found.

# The rindex() method is almost the same as the rfind() method. See example below.

# Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

# Where in the text is the last occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)

# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)

# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.rfind("q"))
print(txt.rindex("q"))