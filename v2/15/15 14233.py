from itertools import *

def f(x):
    A=a1<=x<=a2
    P=17<=x<=46
    Q=22<=x<=57
    return (not A)<=((P and Q)<=A)


Ox=[i/4 for i in range(16*4,59*4)]
n=[]

for a1,a2 in combinations(Ox,2):
    if all(f(x) for x in Ox):
        n.append(a2-a1)

print(round(min(n)))