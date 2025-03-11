#1
arr = list(map(int, input().split()))
k = int(input())
for i in range(k):
    max_val = max(arr)  
    arr.remove(max_val)
print(max_val)

l=list(map(int,input().split()))
k=int(input())
for i in range(k-1):
    maxi=float("-inf")
    for i in l:
        if i>maxi:
            maxi=i
    l.remove(maxi)
print(max(l))
#2
def is_disarium(n):
    digits = list(map(int, str(n)))
    sum_of_powers = sum(digit ** (index + 1) for index, digit in enumerate(digits))
    return sum_of_powers == n
num = int(input("Enter a number: "))
if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is NOT a Disarium number.")