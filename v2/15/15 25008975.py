from itertools import *


def f(x):
    P=5<=x<=30
    Q=14<=x<=23
    A=a1<=x<=a2
    return (P==Q)<=(not A)


Ox=[i/4 for i in range(3*4,33*4)]
n=[]


for a1,a2 in combinations(Ox,2):
    if all(f(x) for x in Ox):
        n.append(a2-a1)
print(n)
print(round(max(n)))