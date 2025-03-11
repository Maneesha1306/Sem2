#1
from abc import ABC,abstractmethod
class AbstractBase(ABC):
    @abstractmethod
    def welcome(self):
        pass
    @abstractmethod
    def test_data(self,name):
        pass
    @abstractmethod
    def count_vowels(self,name):
        pass
    @abstractmethod
    def cal_grade(self,name,mark1,mark2):
        pass
class Student(AbstractBase):
    def welcome(self):
        print("Welcome to WTS!\nWe wish you the best")
    def test_data(self,name):
        print(f"Welcome {name}!\nHave a nice day!")
    def count_vowels(self,name):
        vowels='aeiou'
        vowel_count=0
        name_lower=name.lower()
        vowel_count={v: name_lower.count(v) for v in vowels if v in name_lower} #stores the vowel and its count in dictionary
        total_vowels=sum(vowel_count.values()) #cals total count of vowels in values
        print(f"Count of Vowels are: {total_vowels}")
        for vowel,count in vowel_count.items():
            print(f"{vowel} : {count}")
    def cal_grade(self,name,mark1,mark2):
        total_mark=mark1+mark2
        if total_mark>95:
            grade='E'
        elif total_mark<75 and total_mark>=80:
            grade='A+'
        elif total_mark>=75 and total_mark<=80:
            grade='A'
        elif total_mark>60 and total_mark<=50:
            grade='B'
        else:
            grade='F'
        print(f"{name} Total Marks: {total_mark} | Grade: {grade}")
s=Student()
s.welcome()
name=input("Enter your name: ")
s.test_data(name)
s.count_vowels(name)
mark1=int(input("Enter your mark1: "))
mark2=int(input("Enter your mark2: "))
s.cal_grade(name,mark1,mark2)
#2
def break_num(in_str):
 result=""
 for char in in_str:
    if char.isdigit():
        print("Your Output will Break here - ",result)
        result+=char
    else:
        print("Your Output - ",result)

def skip_num(in_string):
 result=""
 for char in in_str:
    if char.isdigit():
        continue
    result+=char
 print("Your Output will continue here - ",result)
in_string=input("Enter your input: ")
break_num(in_string)
in_str=input("Enter your input: ")
skip_num(in_str)