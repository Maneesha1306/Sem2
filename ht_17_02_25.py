'''1. Write a function that takes two dictionaries and merges them into one.
'''
def merge_dictionary(d1,d2):
    new_d={}
    for i,j in d1.items():
        new_d[i]=j
    for i,j in d2.items():
        new_d[i]=j
    print(new_d)
d1=eval(input())
d2=eval(input())
merge_dictionary(d1,d2)
'''Write a function that takes two lists and returns a dictionary with common elements
as keys and their counts as values.'''
def dictionary():
    l1=eval(input())
    l2=eval(input())
    d={}
    for i in l1:
        if i not in d and i in l2:
          d[i]=1
        elif i in d and i in l2:
           d[i]+=1
    print(d)
dictionary()
'''Write a function that takes a list of (key, value) tuples and converts it into a
dictionary'''
def tuple_c():
    l1=eval(input())
    new_d={}
    for i in l1:
        new_d[i[0]]=i[1]
    print(new_d)
tuple_c()
 