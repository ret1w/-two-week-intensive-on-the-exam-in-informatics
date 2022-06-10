from itertools import *

a=list(product("ВИШНЯ",repeat=6))
count=0
for x in a:
    s=''.join(x)
    if s.count("В")<=1 and s[0]!="Ш" and (s[-1] not in "ИЯ"):
        count+=1
        print(s)
print(count)