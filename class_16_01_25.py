#Question1 
arr = list(map(int,input("Enter the list : ").split())) 
n=len(arr)+1 
total = n * (n + 1) // 2  # 5*(6)//2=30//2=15 
num = sum(arr) #12  
missing = total - num  #15-12=3 
print("Missing number is : ", missing) 
 
#Question2 
arr = list(map(int,input("Enter the list : ").split())) 
repeat= {}   
same = [] 
for num in arr: 
    if num in repeat: 
        same.append(num)   
    else: 
        repeat[num] = 1 
print("Duplicates are : ", same) 
 
#Question3 
def is_sorted(arr): 
    for i in range(len(arr) - 1): 
        if arr[i] > arr[i + 1]: 
            return False 
    return True 
 
user_input = input("Enter the numbers separated by spaces: ") 
arr = list(map(int, user_input.split())) 
 
print(is_sorted(arr)) 
 
#Question4 
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4] 
count = {} 
majority_element = "No majority element" 
 
for num in arr: 
    count[num] = count.get(num, 0) + 1   
    if count[num] > len(arr) // 2:   
        majority_element = num 
        break 
 
print("Majority element is:", majority_element) 
 
#Question5 
def is_balanced_array(arr): 
    total_sum = sum(arr) 
    left_sum = 0 
     
    for i in range(len(arr)): 
        right_sum = total_sum - left_sum - arr[i] 
        if left_sum == right_sum: 
            return True 
        left_sum += arr[i] 
     
    return False 
arr=list(map(int,input("Enter the list : ").split())) 
print(is_balanced_array(arr)) 

 
#Question6 
arr = list(map(int,input("Enter the list : ").split())) 
target = 10 
pairs = [] 
seen = set()   
 
for num in arr: 
    diff = target - num   
    if diff in seen:   
        pairs.append((diff, num))   
    seen.add(num)  
 
print("Pairs that sum to target:", pairs)