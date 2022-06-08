from itertools import *

a=list(product("УЧЕНИК",repeat=5))
count=0
for x in a:
    s=''.join(x)
    if s[0]=="У" and s[-1]=="К":
        count+=1
print(count)