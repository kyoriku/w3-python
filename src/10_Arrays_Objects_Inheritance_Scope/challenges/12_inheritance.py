# Add 'graduationyear' as a property to the to the Student class.

# Requirements
# Student should have an additional attribute graduationyear.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    #Add 'graduationyear' as a property 
    self.graduationyear = year

#After adding 'graduationyear' as a property, the lines below should work
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)