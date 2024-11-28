#1
class Student:
    def __init__(self,name,rollno,sub1,sub2,sub3):
        self.name=name
        self.rollno=rollno
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def calc_grade(self):
        print("Name:",self.name)
        print("Roll no.:",self.rollno)
        percentage=((self.sub1+self.sub2+self.sub3)/300)*100
        if percentage>=85:
            print("Grade S")
        elif percentage>=75:
            print("Grade A")
        elif percentage>=65:
            print("Grade B")
        elif percentage>=55:
            print("Grade C")
        elif percentage>=50:
            print("Grade D")

s=Student("Abi","AI025",97,76,89)
s.calc_grade()

#2
class Student:
    def __init__(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Grade: {self.grade}")
    
    def __del__(self):
        print(f"Student object for {self.name} is being deleted.")

student = Student("Abi", 19, "Computer Science", "A")
student.display()
del student
