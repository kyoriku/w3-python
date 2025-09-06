# Write a Python program that uses two the two predefined sets. The program should perform a set difference operation to find the elements present in set1, but not present in set2.

# Requirements
# `set1` and `set2` are kept as they are.
# Use the `difference()` method to find the items that are only present in `set1`.
# `set3` should only contain items 'banana' and 'cherry'.

# Keep these sets as they are
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# Write your code to find the difference here
set3 = set1.difference(set2)
print(set3)