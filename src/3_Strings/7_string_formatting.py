# F-Strings
txt = f"The price is 49 dollars"
print(txt)

# Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {95:.2f} dollars"
print(txt)

# Perform Operations in F-Strings
txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

# Execute Functions in F-Strings
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048
txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# More Modifiers
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# String format()
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values
price = 49
count = 3
itemno = 5
txt = "It costs {} dollars for {} pieces of item number {}"
print(txt.format(price, count, itemno))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers
quantity = 30
itemno = 765
price = 99
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))