def f(x): return (x%a==0)<=((not x%21==0) +(x%35==0))


for a in range(1,2000):
    if all(f(x) for x in range(10000)):
        print(a)