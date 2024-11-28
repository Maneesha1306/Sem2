class Inventory:
    def getInventoryInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
        self.count=int(input("Enter the Count:"))
    def displayInventoryInfo(self):
        print("ID = ",self.id,"\nName = ",self.name,"\nCount = ",self.count)

class Perks(Inventory):
    def getDetails(self):
        self.getInventoryInfo()
        self.price=int(input("Enter the price: "))
    def displayInfo(self):
        self.displayInventoryInfo()
        print("Price = ",self.price)

p=Perks()
p.getDetails()
p.displayInfo()
