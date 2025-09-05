# The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
# Meaning: The returned set contains a mix of items that are not present in both sets.
# As a shortcut, you can use the ^ operator instead, see example below.

# Syntax
# set.symmetric_difference(set1)

# Shorter Syntax
# set ^ set1

# Parameter Values
# Parameter | Description
# set1      | Required. The set to check for matches in

# Return a set that contains all items from both sets, except items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# Use ^ as a shortcut instead of symmetric_difference():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x ^ y
print(z)