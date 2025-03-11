#1
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_features(self):
        print(f"Make: {self.make}, \nModel: {self.model},\nYear: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors, trunk_capacity):
        Vehicle.__init__(self,make, model, year)
        self.doors = doors
        self.trunk_capacity = trunk_capacity
    def car_display_features(self):
        self.display_features()
        print(f"Doors: {self.doors},\nTrunk Capacity: {self.trunk_capacity}L")

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, axles):
        Vehicle.__init__(self,make, model, year)
        self.cargo_capacity = cargo_capacity
        self.axles = axles
    def truck_display_features(self):
        self.display_features()
        print(f"Cargo Capacity: {self.cargo_capacity}kg,\nAxles: {self.axles}")

class PickupTruck(Car, Truck):
    def __init__(self, make, model, year, doors, trunk_capacity, cargo_capacity, axles):
        Car.__init__(self, make, model, year, doors, trunk_capacity)
        Truck.__init__(self, make, model, year, cargo_capacity, axles)
    def PT_display_features(self):
        print(f"PickupTruck Features:")
        print("Car Features:")
        self.car_display_features()
        print("Truck Features:")
        self.truck_display_features()

pickup = PickupTruck("Ford", "Ranger", 2024, doors=4, trunk_capacity=500, cargo_capacity=1500, axles=2)
print(pickup.PT_display_features())


#2
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    def display_info(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}")

class Electronics(Product):
    def __init__(self, product_id, name, price, warranty_period, brand):
        super().__init__(product_id, name, price)
        self.warranty_period = warranty_period
        self.brand = brand
    def elec_display_info(self):
        self.display_info()
        print(f"Warranty: {self.warranty_period} years, Brand: {self.brand}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

    def cloth_display_info(self):
        self.display_info()
        print(f"Size: {self.size}, Material: {self.material}")

laptop = Electronics(product_id=101, name="Laptop", price=1500, warranty_period=2, brand="Dell")
laptop.elec_display_info()

tshirt = Clothing(product_id=202, name="T-Shirt", price=25, size="M", material="Cotton")
tshirt.cloth_display_info()

    # Display

