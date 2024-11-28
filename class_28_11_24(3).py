class Inventory:
    def getInventoryInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
        self.count=int(input("Enter the Count:"))
    def displayInventoryInfo(self):
        print("ID = ",self.id,"\nName = ",self.name,"\nCount = ",self.count)

p=Inventory()
p.getDetails()
p.displayInfo()
