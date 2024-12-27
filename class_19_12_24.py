import re
word="Simple regular expression example regular"
result= re.findall("gula",word)
print(result)

space=re.search("\s",word)
print("First space:",space.start())