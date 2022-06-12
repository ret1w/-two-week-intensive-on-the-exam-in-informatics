from itertools import *

a=list(product("КРОТ",repeat=6))
counter=0
for x in a:
    s=''.join(x)
    if s.count('О')==1:
        counter+=1
print(counter)

