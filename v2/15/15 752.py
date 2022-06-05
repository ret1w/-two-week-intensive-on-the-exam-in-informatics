a=set()


def f(x):
    A= x in a
    B = x in {3, 6, 9, 12}
    C= x in {1,2,3,4,5,6}
    return not((not(A)) and B) or (not(C))


for x in range(1000):
    if f(x)==0:
        a.add(x)
print(a)