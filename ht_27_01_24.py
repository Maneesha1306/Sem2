n=int(input("Enter no. of elements:"))
a=[]
for i in range(n):
    a.append(int(input()))
print("Inverse array:",a[::-1])
print("Non-Inverse array:",a)

