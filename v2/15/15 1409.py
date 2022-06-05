a=set()


def f(x):
    A= x in a
    P= x in {i for i in range(2,21,2)}
    Q= x in {i for i in range(3,31,3)}
    R= x in {i for i in range(12,60,12)}
    return (not A) <= ((P and Q)<=R)


for x in range(1000):
    if f(x)==0:
        a.add(x)

print(a)