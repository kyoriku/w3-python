# Implement polymorphic behaviour using classes in Python. Make sure the Car class is a child class of the Vehicle class, and that it does not override anything it inherits from the Vehicle class. Override the move method in Boat to output "Sail!" and in Plane to output "Fly!".

# Requirements
# The Car class should inherit both the `__init__()` and the `move()` methods from the Vehicle class.
# The Boat's move method should print 'Sail!'.
# The Plane's move method should print 'Fly!'.

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    
  def move(self):
    print("Moving...")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self, speed=10):
    print(f"Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()