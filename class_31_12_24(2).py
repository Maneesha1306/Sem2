def perm(s):
    if len(s)<=1:
        return s
    s=list(s)
    p=[]
    for i in range(len(s)):
        c=s[i]
        r=s[:i]+s[i+1:]
        for j in perm(r):
            p.append(c+j)
    return p
p=perm("xyz")
print(p)