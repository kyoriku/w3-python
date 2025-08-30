# Expand upon an existing list by adding elements from a tuple. Your task is to use the extend method to add all items from a tuple to a list.

# Requirements
# The list should be extended with the elements 'kiwi' and 'orange', using the `extend()` method.
# The list should have no duplicates of its original items.
# The list should have a total of 5 items after extension.

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

# Use the extend method on thislist to add the items from thistuple
thislist.extend(thistuple)

print(thislist)