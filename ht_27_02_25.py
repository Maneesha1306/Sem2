class Vehicle:
    def fuelType(self):
        return "General Fuel"
class Car(Vehicle):
    def fuelType(self):
        return "Petrol or Diesel"
class Bike(Vehicle):
    def fuelType(self):
        return "Petrol"
    
c=Car()
b=Bike()
print(c.fuelType())
print(b.fuelType())