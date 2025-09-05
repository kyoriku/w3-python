# The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
# As a shortcut, you can use the ^= operator instead, see example below.

# Syntax
# set.symmetric_difference_update(set1)

# Shorter Syntax
# set ^= set1

# Parameter Values
# Parameter | Description
# set1      | Required. The set to check for matches in

# Remove the items that are present in both sets, AND insert the items that is not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# Use ^= as a shortcut instead of symmetric_difference_update():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x ^= y
print(x)