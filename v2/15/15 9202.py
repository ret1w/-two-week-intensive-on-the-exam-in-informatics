a=set(range(1000))

def f(x):
    A= x in a
    P= x in {i for i in range(2,21,2)}
    Q= x in {i for i in range(3,31,3)}
    return (A<=P) or ((not Q)<= (not A))


for x in range(1000):
    if f(x)==0:
        a.remove(x)
print(len(a))