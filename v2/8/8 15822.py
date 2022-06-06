from itertools import *

l=list(product("АЕКР",repeat=4))
count=0
for i in range(len(l)):
    count+=1
    x=''.join(l[i])
    if "А" not in x:
        print(count)
        break