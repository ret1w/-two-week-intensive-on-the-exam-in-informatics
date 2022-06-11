from itertools import *

a=list(product("АБКЛУ",repeat=4))
counter=0
for x in a:
    counter+=1
    s=''.join(x)
    if any(s.count(j)>=2 for j in "АБКЛУ"): ...
    else: print(x,s,counter)