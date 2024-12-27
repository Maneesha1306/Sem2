class Student:
    __Id=0
    def __init__(self,name):
        self.__name=name#private 
    def display(self):
        print(self.__name)
n=input("Enter name:")
s=Student(n)
s.__Id=int(input())
print(s.Id)