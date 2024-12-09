class Employee:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print("Name:",self.name)


class Designation(Employee):
    def __init__(self,name,desgn):
        Employee.__init__(self,name)
        self.desgn=desgn
    def display_desgn(self):
        print("Designation:",self.desgn)


class Salary(Employee):
    def __init__(self,name,salary):
        Employee.__init__(self,name)
        self.salary=salary
    def display_sal(self):
        print("Salary:",self.salary)

class Individual(Designation,Salary):
    def __init__(self,name,salary,desgn):
        Designation.__init__(self,name,desgn)
        Salary.__init__(self,name,salary)
    def display_all(self):
        print("#Employee class")
        self.display_name()
        print("#Designation class")
        self.display_desgn()
        print("#Salary class")
        self.display_sal()


emp=Individual("Amal",35000,"Lab assisstant")
emp.display_all()