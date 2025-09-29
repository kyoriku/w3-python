# Make the myfunc function return a lambda function. With the correctly returned lambda function, the result of running mytripler(11) should be 33.

# Requirements
# Variable `mytripler` should be a lambda multiplying by 3.

def myfunc(n):
  # Return a lambda function
  # so that "mytripler" is a function
  # that triples the input argument.
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
# The resulting print should be "33"