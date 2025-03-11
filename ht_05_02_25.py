#1
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))  
print(longest_common_prefix(["dog", "racecar", "car"]))     

#2
def is_subsequence(s, t):
    it = iter(t)
    return all(char in it for char in s)

# Example usage
print(is_subsequence("abc", "ahbgdc"))  
print(is_subsequence("axc", "ahbgdc"))

