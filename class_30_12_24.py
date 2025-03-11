'''import sys
a=[]
b=a
print(sys.getrefcount(a))
'''
'''import gc
collected=gc.collect()
print(collected)
'''

import gc
gc.enable()
gc.disable()
l1=[1,2,3]
d1={"1":1,"2":2}
s1="Garbage collection"
del l1
del d1
del s1
gc.set_threshold(1,2,2)
print(gc.get_threshold())
print(gc.collect())