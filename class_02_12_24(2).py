class Employee:
    def __init__(self,name,Id):
        self.name=name
        self.Id=Id
    def display(self):
        print("Name:",self.name,"\nID:",self.Id)

class Manager(Employee):
    def __init__(self,name,Id,Salary,Desg):
        super().__init__(name,Id)
        self.Salary=Salary
        self.Desg=Desg
    def displayManager(self):
        self.display()
        print("Salary:",self.Salary)
        print("Designation:",self.Desg)

class Developer(Employee):
    def __init__(self,name,Id,Salary,Desg):
        super().__init__(name,Id)
        self.Salary=Salary
        self.Desg=Desg
    def displayDeveloper(self):
        self.display()
        print("Salary:",self.Salary)
        print("Designation:",self.Desg)

m=Manager("James","E623D",50000,"Manager")
m.displayManager()

d=Developer("John","R382H",45000,"Developer")
d.displayDeveloper()
