# Write a Python code that checks if number is even or odd. Print "even" if numberis even and "odd" if numberis odd. Use the modulo operator (%) to check if number % 2 equals 0 for even numbers.

# Requirements
# Should print "odd" for odd number
# Should print "even" for even number

# Do not modify this
import os
number = int(os.environ.get("number", 12))

# Check if number is an odd or even number and print "odd" or "even" accordingly
if number % 2 == 0:
  print("even")
else:
  print("odd")