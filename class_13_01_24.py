arr=list(map(int,input().split()))
n = len(arr)
ini_index = 0

for i in range(n):#0
    if arr[i] != 0:
        arr[ini_index], arr[i] = arr[i], arr[ini_index]
        ini_index += 1

print(arr)


n = len(arr)
# Pointer for the position of the next zero
zero_index = n - 1

# Traverse the array from the end
for i in range(n - 1, -1, -1):
    if arr[i] != 0:
        # Swap the current element with the zero_index position
        arr[zero_index], arr[i] = arr[i], arr[zero_index]
        zero_index -= 1

print(arr)




def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit
price=[7,1,5,3,6,4]
print(max_profit(price))