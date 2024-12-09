class Stud_details:
    def __init__(self,name,rollno,classes):
        self.name=name
        self.rollno=rollno
        self.classes=classes
    def display_details(self):
        print("Name:",self.name,"\nRoll No.:",self.rollno,"\nClass:",self.classes)

class Marks(Stud_details):
    def __init__(self, name, rollno, classes,m1,m2,m3):
        super().__init__(name, rollno, classes)
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def display_perc(self):
        total=self.m1+self.m2+self.m3
        perc=(total/300)*100
        self.display_details()
        print(f"Percentage:{perc:0.2f}")

n=input("Enter name:")
r=input("Enter rollno:")
c=input("Enter class:")
m1=int(input("Enter mark 1:"))
m2=int(input("Enter mark 2:"))
m3=int(input("Enter mark 3:"))
s=Marks(n,r,c,m1,m2,m3)
s.display_perc()