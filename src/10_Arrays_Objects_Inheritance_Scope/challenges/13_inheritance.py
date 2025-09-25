# Write the missing code line so that the Student class init() function inherits the constructor from the Person class. This means that when an instance of the Student class is created, it should initialise using the constructor of the Person class.

# Requirements
# The `Student` class should inherit the `__init__` function from `Person`.

class Person:  
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):  
  def __init__(self, fname, lname):
    #Make the Student __init__ function inherit the Person's __init__ function
    super().__init__(fname, lname)


x = Student("Mike", "Olsen")

x.printname()