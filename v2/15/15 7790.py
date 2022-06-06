from itertools import *
def f(x):
    A= a1<=x<=a2
    P=7<=x<=14
    Q=9<=x<=11
    return (P==Q)<=(not A)

Ox=[i/4 for i in range(6*4,16*4)]
n=[]

for a1,a2 in combinations(Ox,2):
    if all(f(x) for x in Ox):
        n.append(a2-a1)
print(round(max(n)))