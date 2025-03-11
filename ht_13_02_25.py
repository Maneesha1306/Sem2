#1
def print_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
print_pattern(5)

#2
def check_prime(n):
    if n==2:
        print("prime")
    else:
        for i in range(2,n):
            if n%i==0:
                print("Non-prime")
                break
        else:
            print("Prime")
check_prime(2)
check_prime(5)
check_prime(6)