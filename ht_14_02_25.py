class Empl:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        print(f"Name:{self.name}\nEmployee ID:{self.emp_id}\nSalary:{self.salary}")
    def calculate_yearly_salary(self):
        print("Annual salary:",self.salary*12)

empl1=Empl("Alice","E23jfgr",30000)
empl1.display()
empl1.calculate_yearly_salary()

class Employee:
    def __init__(self,name,emp_id,dept):
        self.name=name
        self.emp_id=emp_id
        self.dept=dept
    def display_info(self):
        print(f"Name:{self.name}\nEmployee ID:{self.emp_id}\nDepartment:{self.department}")

class FullTimeEmployee(Employee):
    def __init__(self,name,emp_id,dept,sal):
        super.__init__(self,name,emp_id,dept)
        self.sal=sal
    def calculate_annual_salary(self):
        self.annual_salary=self.sal*12
    def display_full_time_info(self):
        self.display_info()
        print(f"Monthly salary:{self.sal}\nAnnual salary:{self.annual_salary}")
class PartTimeEmployee(Employee):
    def __init__(self,name,emp_id,dept,hourly_rate,hours_worked):
        super.__init__(self,name,emp_id,dept)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        self.salary=self.hourly_rate*self.hours_worked
    def display_part_time_info(self):
        self.display_info()
        print(f"Hourly rate:{self.hourly_rate}\nHours worked:{self.hours_worked}\nSalary:{self.salary}")
