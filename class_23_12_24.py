'''#1
user_name=input("Username:")
passwd=input("Passwd:")
def login_attempt():
    print("****LOGIN****")
    for i in range(5):
        username=input("Username:")
        password=input("Password:")
        if username==user_name and password==passwd:
            print("Login successful")
            break
    else:
        print("Login denied! Account locked")
        
#2
l=eval(input("Enter list:"))
s=set(l)
l=list(s)
l.sort(reverse=True)
print("Manipulated List:",l)

#3
n=int(input())
sum=0
while n>=0:
    a=n%10
    sum+=a
    n=n//10
print("Sum of digits:")'''

#4
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
l1=[]
for i in range(n1):
    l1.append(input("l1:"))
l2=[]
for i in range(n2):
    l2.append(input("l2:"))
for i in range(n1):
    if l1[i] in l2:
        print(l1[i])


#5
s=input("Enter String:")
s=s.split()
print("Number of words:",len(s))

#6
elements=eval(input("Enter list:"))
n=len(elements)
for i in range(n):
    for j in range(0,n-i-1):
        if elements[j]>elements[j+1]:
            elements[j],elements[j+1]=elements[j+1],elements[j]
print(elements)

#7
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self):
        amt= int(input("Enter amount to be deposited:"))
        if amt>0:
            self.balance+=amt
            print("Amount deposited")
        else:
            print("enter valid amount")
    def withdraw(self):
        amt= int(input("Enter amount to withdrawn:"))
        if amt>=self.balance:
            self.balance-=amt
            print("Amount Withdrawn")
        else:
            print("Insufficient funds")
    def check(self):
        print("Balance:",self.balance)
a=BankAccount(50000)
a.deposit()
a.withdraw()
a.check()

#8
import re
email=input("Enter the email id:")
ex=ex=r'^[a-z0-9._%+-]+@gmail\.com$'
if re.match(ex,email):
    print("Valid")
else:
    print("Not a valid")

#9
import re

def extract_phone_numbers(text):
    phone_pattern = r'\b\d{10}\b|\b(?:\d{3}[-.\s]?\d{3}[-.\s]?\d{4})\b'
    return re.findall(phone_pattern, text)
text=input()
phone_numbers = extract_phone_numbers(text)
print("Extracted phone numbers:", phone_numbers)

#10
import re
text=input("Enter the text:")
ex=r'#\w+'
result=re.findall(ex,text)
print(result)
