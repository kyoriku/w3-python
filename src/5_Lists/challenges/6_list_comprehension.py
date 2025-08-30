# Use a list comprehension to filter out the string 'apple' from the given list of fruits and return a new list. Assign this new list to a variable named newlist.

# Requirements
# fruits should initially contain five specific fruits including 'apple'.
# newlist should exclude 'apple'.
# newlist should have four elements after excluding 'apple'.

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [fruit for fruit in fruits if fruit != 'apple'] # Use list comprehension to filter out 'apple'
