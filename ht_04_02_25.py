#1
s=input()
s=s.split()
print(len(s[-1]))

s=input().strip()
n=0
for i in s[::-1]:
    if i==" ":
        break
    n+=1
print(n)

#2
a=input()
b=input()
c=bin(int(a,2) + int(b, 2))[2:]
print(c)

