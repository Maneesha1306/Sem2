'''#1
n=int(input())
for i in range(1,n+1):
    print(i,end=' ')
    for j in range(n-1,n-i,-1):
        i=i+j
        print(i,end=' ')
    print()

#2
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
n=n/2
d=set()
for i in a:
    if a.count(i)>n:
        d.add(i)
for i in d:
    print("op:",i)


#3
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def avg_marks(self):
        return sum(self.marks.values())/len(self.marks)
def topper(students):
    t=None
    a=-1
    for i in students:
        if i.avg_marks()>a:
            a=i.avg_marks()
            t=i
    print(f"Topper:{t.name},Roll No.:{t.rollno},Avg Marks:{a}")
n=int(input("Enter no of students:"))
stu_obj=[]
for i in range(n):
    n=input("Enter name:")
    r=input("Enter rollno:")
    m=eval(input("Enter marks as dictionary:"))
    s=Student(n,r,m)
    stu_obj.append(s)
topper(stu_obj)
'''

#4
def product_info(**p):
    for i in p:
        print(f'{i}:{p[i]}')
        if "discount" in p:
            fp=p["price"]-(p["price"]*)
