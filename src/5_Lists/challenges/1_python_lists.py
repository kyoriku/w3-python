# Write Python code to create a list of integers from 1 to 10 and square each number in the list.

# Requirements
# The program should generate a list of numbers from 1 to 10.
# The program should correctly square each number in the list.
# The program should print the resulting list.

# Createa a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Square each number in the list
squared_numbers = [x ** 2 for x in numbers]

# Print the resulting list
print(squared_numbers)