def hollow_pyramid(n):
    for i in range(1, n+1):
        space = "_" * (n - i)  # space calculation for the first row
        if i == 1:
            print(space + "*")
        elif i == n:
            print("*" * (2 * n - 1))  # 2*5-1 = 9
        else:
            print(space + "*" + "_" * (2 * i - 3) + "*")

n = int(input())  # Taking user input
hollow_pyramid(n)  # Function call



