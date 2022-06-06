a=set()

def f(x):
    A = x in a
    B = x in {2,4,6,8,10,12}
    C = x in {4,8,12,16}
    return B <= ((C and (not A))<=(not B))


for x in range(1000):
    if f(x) == 0:
        a.add(x)
print(sum(a))
