class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_empl_info(self):
        print(f"Name:{self.name}\nAge:{self.age}")

class Manager(Employee):
    def __init__(self,name,age,eid):
        super().__init__(name,age)
        self.eid=eid
    def display_manager(self):
        self.display_empl_info()
        print("E_id:",self.eid)

class Developer(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def display_developer(self):
        self.display_empl_info()
        print("Department:",self.dept)

class Teamleader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
        Employee.__init__(self,name,age)
        self.eid=eid
        self.dept=dept
        self.teamsize=teamsize
    def display_team(self):
        print("TeamSize:",self.teamsize)

tl=Teamleader("Abi","35","d3543","Developer",7)
tl.display_empl_info()
tl.display_manager()
tl.display_developer()
tl.display_team()