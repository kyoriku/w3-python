# Use f-string to create a message based on a given price.

# If the price is greater than 50, the message should say 'It is expensive', otherwise 'It is cheap'.

# Requirements
# Variable 'price' is 49.
# The 'txt' variable should contain 'expensive' if price is greater than 50.
# The 'txt' variable should contain 'cheap' otherwise.

# The price
price = 49
# Use if...else inside f-string 
txt = f"It is {'expensive' if price > 50 else 'cheap'}"
# Keep this print statement as it is
print(txt)