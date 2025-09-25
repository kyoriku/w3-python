# Change the global variable x to 200 from inside the function, using the global keyword.

# Requirements
# Variable `x` should be defined as 200 after calling myfunc.

x = 300

def myfunc():
  #Make myfunc change the value of the x variable outside the function
  global x
  x = 200

myfunc()

print(x)