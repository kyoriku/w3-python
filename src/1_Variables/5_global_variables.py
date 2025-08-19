# Create a variable outside of a function, and use it inside the function
x = "awesome"

def print_global_variable():
  print("Python is " + x)

print_global_variable()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def print_local_variable():
  x = "fantastic"
  print("Python is " + x)

print_local_variable()

print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:
def change_global_variable():
  global x
  x = "fantastic"

change_global_variable()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def update_global_variable():
  global x
  x = "fantastic"

update_global_variable()

print("Python is " + x)