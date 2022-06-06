a=set()


def f(x):
    A= x in a
    P= x in {i for i in range(1,22,2)}
    print(P)
    Q= x in {i for i in range(3,31,3)}
    return (P<=A) or ((not A) <=(not Q))


for x in range(10000):
    if f(x)==0:
        a.add(x)
print(sum(a))