string=input()
def fun1(string):
    s=''
    for i in string:
        if "A"<=i<="Z":
            c=ord(i)
            s+=chr(c+32)
        else:
            s+=i
    print(s)
fun1(string)
char=input()
if "a"<=char<="z":
    c=ord(char)
    print(chr(c-32))


def lowercase(ch):
    p=ord(ch)
    q=chr(p+32)
    print(q,end='')
def uppercase(ch):
    x=ord(ch)
    y=chr(x-32)
    print(y,end='')
str1=input()
for i in str1:
    if 'A'<=i<='Z':
        lowercase(i)
    elif 'a'<=i<='z':
        uppercase(i)