'''#reverse a string without built-in function
s=input().strip()
length=0
for i in s:
    length+=1
rev_str=''
for i in range(-1,-length-1,-1):#length-1,-1,-1
    rev_str+=s[i]
print(rev_str)
'''
#replace letter
s=input()
l1=input()
l2=input()
def replace(s,l1,l2):
    replaced=''
    for i in s:
        if i==l1:
            replaced+=l2
        else:
            replaced+=i
    print(replaced) 
replace(s,l1,l2)