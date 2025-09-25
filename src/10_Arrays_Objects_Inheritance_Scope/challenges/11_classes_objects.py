# Write the init() function and myfunc() method for the Person class.

# The init() method takes 'name' (string) and 'age' (integer) to create an instance of the Person class.
# The myfunc() method prints "Hello my name is " followed by the person's name.
# Instantiate a Person object with the name "John" and age 36.
# Then call the myfunc method on that object.

# Requirements
# The `__init__` method accepts `name` and `age` as parameters, and creates a new object with those properties.
# The `myfunc` method prints a greeting containing 'hello' and 'john' (case insensitive).
# Use the `Person` class to create a person `p1`, with name "John", age 36.
# Call the 'myfunc()' method from the 'p1' Person instance.

class Person:
  def __init__(self, name, age):
    # Initialize name and age here
    self.name = name
    self.age = age

  def myfunc(self):
    # Print name with a "Hello" greeting here
    print("Hello my name is " + self.name)

# Create a Person p1, with name "John", age 36.
# p1 = ...
p1 = Person("John", 36)
# Call the myfunc method to print the persons details.
p1.myfunc()