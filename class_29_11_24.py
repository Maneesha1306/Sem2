class Employee:
    def __init__(self,name,Id,position):
        self.name=name
        self.Id=Id
        self.position=position
    def display(self):
        print("Name:",self.name,"\nId:",self.Id,"\nPosition:",self.position)
class Address:
    def __init__(self,city,state,country):
        self.city=city
        self.state=state
        self.country=country
    def displayAddress(self):
        print("City:",self.city,"\nState:",self.state,"\nCountry:",self.country)

class EmployeeDetails(Employee,Address):
    def __init__(self,name,Id,position,city,state,country):
        super().__init__(name,Id,position)
        Address.__init__(self,city,state,country)
    def displayEmp(self):
        self.display()
        self.displayAddress()
empl=EmployeeDetails("Abi",23452,"Manager","Banglore","Karnataka","India")
empl.displayEmp()
