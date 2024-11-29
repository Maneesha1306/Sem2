#1
class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("Name:",self.name)
class Student(Person):
    def __init__(self,name,stud_id):
        super().__init__(name)
        self.stud_id=stud_id
    def show_student_id(self):
        self.show_name()
        print("Student ID:",self.stud_id)

s=Student("Abi","Ed263b")
s.show_student_id()

#2
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def display_dept(self):
        self.display_details()
        print("Department:",self.dept)

e=Manager("Abi",45000,"Sales")
e.display_dept()
