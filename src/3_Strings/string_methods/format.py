# The format() method formats the specified value(s) and insert them inside the string's placeholder.

# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

# The format() method returns the formatted string.

# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# Using different placeholder values:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)