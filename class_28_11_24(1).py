class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the id:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\nName=",self.name)

class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary:"))
    def displayInfo(self):
        self.displayEmployeeInfo()
        print("salary=",self.sal)

empl=Perks()
empl.getDetails()
empl.displayInfo()
