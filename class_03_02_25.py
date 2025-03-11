# lambda <arguments>:<expression>
add=lambda a,b,c:a+b+c
print(add(1,2,3))

multiply=lambda a,b:a*b
print(multiply(2,3))

l=list(map(int,input().split()))
sq=lambda li:[i**2 for i in li]
print(sq(l))

l2=list(map(int,input().split()))
even=filter(lambda x:x%2==0,l2)
print(list(even))

t=[(1,2),(6,3),(4,1)]
tl=sorted(t,key=lambda x:x[0])
print(tl)

name=["abc","def","ghi"]
sal=[1500,2000,1000]
s=zip(name,sal)
sort=sorted(s,key=lambda k:k[1])
print(sort)

l3=list(map(int,input().split()))
odd=filter(lambda x:x%2!=0,l3)
print(l3)

l4=list(map(int,input().split()))
cube=map(lambda x:x**3,l4)
print(list(cube))

