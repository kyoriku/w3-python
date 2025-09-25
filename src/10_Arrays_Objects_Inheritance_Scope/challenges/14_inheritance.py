# Create an instance 'x' of the Student class, and print that student's graduation year.

# Requirements
# Create an instance 'x' of the Student class.
# Access that student's graduation year and print it.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

# Create an instance 'x' of the Student class here
x = Student("Mike", "Olsen")
# Access that student's graduation year, and print it
print(x.graduationyear)