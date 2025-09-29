# Modify the function so that it only accepts positional arguments, so that keyword-arguments are not accepted.

# Requirements
# Ensure that the `my_function` functions only accepts positional arguments.

def my_function(x, /):
  print(x)

my_function(3) #positional argument
#my_function(x=3) keyword argument