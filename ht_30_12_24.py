import string
class alphanum:
    def __init__(self,s):
        self.s=s
    def numbers(self):
        a=0
        n=0
        sp=0
        for i in self.s:
            if i.isalpha():
                a+=1
            elif i.isdigit():
                n+=1
            elif i in string.punctuation:
                sp+=1
        print("Alphabetic characters:",a)
        print("Numeric characters:",n)
        print("Special character:",sp)
s=input()
c=alphanum(s)
c.numbers()

class string_validation:
    def __init__(self,str):
        self.str=str
    def validate(self):
        alpha=0
        sp=0
        for i in self.str:
            if i.isalpha():
                alpha+=1
            elif i in string.punctuation:
                sp+=1
        if alpha>=1 and sp>=1:
            print("String contains both alphabets and special characters")
        else:
            print("String is not validated")
            
s=input()
c=string_validation()
c.validate()