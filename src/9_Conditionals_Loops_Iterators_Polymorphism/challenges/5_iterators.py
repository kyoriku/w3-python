# Write a Python program that iterates through a tuple mytuple containing the strings "apple", "banana", and "cherry". Use an iterator to print each item in the tuple sequentially.

# Requirements
# Use methods `iter()` and `next()` to iterate through the tuple.
# Ensure items are printed in sequence.

mytuple = ("apple", "banana", "cherry")

# Your code here
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))