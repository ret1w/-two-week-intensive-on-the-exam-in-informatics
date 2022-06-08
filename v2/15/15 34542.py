from itertools import *


def f(x):
    P=1<=x<=39
    Q=23<=x<=58
    A=a1<=x<=a2
    return (P<=(not Q)) <= (not A)


Ox=[i/4 for i in range(0*4,60*4)]
n=[]


for a1,a2 in combinations(Ox,2):
    if all(f(x) for x in Ox):
        n.append(a2-a1)
print(max(n))
print(round(max(n)))

