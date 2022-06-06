def f(x):
    return (x&29!=0)<=((x&12==0)<=(x&a!=0))


for a in range(200):
    if all(f(x) for x in range(1000)):
        print(a)