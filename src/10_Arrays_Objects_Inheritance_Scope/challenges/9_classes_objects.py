# Create a class named Person. The init() function takes name and age as arguments to create a new instance/object of the Person class. Create a new object p1 of Person with the name 'John' and the age 36.

# Requirements
# The __init__() function can create a new object with name and age.
# The instance `p1` should have the `name` variable set to 'John' and `age` set to 36.

# Define the Person class here
class Person:
  def __init__(self, name, age):
    # Initialize the instance variables
    self.name = name
    self.age = age

# Create an instance of Person, name "John", age 36
p1 = Person("John", 36)  # Replace None with an instance