class Person:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
    def displayPerson(self):
        print("Name:",self.Name,"\nAge:",self.Age)

class Employee(Person):
    def __init__(self,Name,Age,ID):
        super().__init__(Name,Age)
        self.ID=ID
    def displayEmployee(self):
        self.displayPerson()
        print("Id:",self.ID)


class Manager(Employee):
    def __init__(self,Name,Age,ID,Salary):
        super().__init__(Name,Age,ID)
        self.Salary=Salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary:",self.Salary)

m=Manager("Diana", 35, "Ef334r",50000)
m.displayManager()
