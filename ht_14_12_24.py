#1
def merge_alternately(word1, word2):
    merged = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    if i < len(word1):
        merged.append(word1[i:])
    if j < len(word2):
        merged.append(word2[j:])
    return ''.join(merged)
print(merge_alternately("abc", "pqr"))    
print(merge_alternately("ab", "pqrs"))    

#2
def can_place_flowers(flowerbed, n):
    count = 0
    length = len(flowerbed)    
    for i in range(length):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
        if count >= n:
            return True    
    return False

print(can_place_flowers([1, 0, 0, 0, 1], 1))  
print(can_place_flowers([1, 0, 0, 0, 1], 2))  
