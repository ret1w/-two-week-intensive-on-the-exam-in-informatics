from itertools import *


a=list(product("АБРТЫ",repeat=5))
count=0
for x in a:
    count+=1
    s=''.join(x)
    if s.count('Ы')==0 and "АА" not in s:
        print(count,s)
        break