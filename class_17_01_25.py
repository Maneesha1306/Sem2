#Question 1 
 
def reverse(string): 
    if len(string)<=0: 
        return string 
    else: 
        return reverse(string[1:])+string[0] 
string=input("Enter the string : ") 
result=reverse(string) 
print("Original string : ",string) 
print("Reversed string : ",result) 
 
#Question 2 
 
def palindrome(srting): 
   if len(string)<=0: 
        return string 
   else: 
        return reverse(string[1:])+string[0] 
string=input("Enter the string : ") 
result=reverse(string) 
print("Original string : ",string) 
print("Reversed string : ",result) 
if string==result: 
    print("It is a Palindrome") 
else: 
    print("it is not a palinrome") 
 
#Question 3 
 
x=int(input("Enter the number : ")) 
n=int(input("Enter the power : ")) 
def power(x,n): 
    if n==0: 
        return 1 
    else: 
        return x*power(x,n-1) 
answer=power(x,n) 
print(answer) 
 
 
 
#Question 4 
 
num=int(input("Enter the number : ")) 
def calculate_sum(num): 
    if n==0: 
        return 0 
    else: 
        return num%10+calculate_sum(num//10) 
result=calculate_sum(num) 
print("Sum of the number : ",result) 
 
#Question 5 
 
n=int(input("Enter the number of elements in the array"))  
arr=[]  
tot=0  
for i in range(n):  
    e=list(map(int,input().split()))  
    arr.append(e)  
for i in range(n):  
    for j in range(n):  
        print(arr[i][j],end=" ")  
    print()  
for i in range(n):  
    for j in range(n):  
        tot+=arr[i][j]  
print(tot)  
  
 
 
#Question 6 
 
n=int(input("Enter the number of elements in the array:"))  
arr=[]  
for i in range(n): 
    e=list(map(int,input().split())) 
    arr.append(e) 
print("Original matrix") 
for i in range(n): 
     for j in range(n): 
        print(arr[i][j],end=" ")  
     print()  
print("Transpose")  
for i in range(n): 
    for j in range(n): 
        print(arr[j][i],end=" ")  
    print()