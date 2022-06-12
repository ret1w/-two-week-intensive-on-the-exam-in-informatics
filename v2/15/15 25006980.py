from itertools import *


def f(x):
    B=18<=x<=52
    C=16<=x<=41
    A=a1<=x<=a2
    return (B<=A) and ((not C) or A)


Ox=[i/4 for i in range(15*4,55*4)]
n=[]


for a1, a2 in combinations(Ox,2):
    if all(f(x) for x in Ox):
        n.append(a2-a1)
print(round(min(n)))