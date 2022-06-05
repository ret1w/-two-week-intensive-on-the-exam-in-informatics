from itertools import *

def f(x):
    P=17<=x<=54
    Q=37<=x<=83
    A=a1<=x<=a2
    return P<=((Q and (not A))<=(not P))


Ox=[i/4 for i in range(16*4,84*4)]
m=[]

for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        m.append(a2-a1)
print(round(min(m)))