class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display_basic_info(self):
        print(f"Name:{self.name}\nAge:{self.age}\nGender:{self.gender}")
    
class Student:
    def __init__(self,course,stud_id):
        self.course=course
        self.stud_id=stud_id
    def display_student_info(self):
        print(f"Course:{self.course}\nStudent ID:{self.stud_id}")

class Extra(Person,Student):
    def __init__(self,name,age,gender,course,stud_id,extra_curricular):
        super().__init__(name,age,gender)
        Student.__init__(self,course,stud_id)
        self.extra_curricular=extra_curricular
    def display_info(self):
        self.display_basic_info()
        self.display_student_info()
        print("Extra curricular:",self.extra_curricular)


name=input("Enter Name:")
age=input("Enter age:")
gender=input("Enter Gender:")
course=input("Enter course:")
s_id=input("Enter Student ID:")
e=input("Enter Extra curricular activity:")
s=Extra(name,age,gender,course,s_id,e)
s.display_info()