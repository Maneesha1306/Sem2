encoded=input()
decoded=""
i=0
while i<len(encoded):
    if encoded[i].isdigit():
        decoded+=encoded[i+1]*int(encoded[i])
        i=i+2
print(decoded)
