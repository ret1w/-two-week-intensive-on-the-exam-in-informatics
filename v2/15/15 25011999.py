def f(x):
    A=( x%15!=0) or ( x%28!=0) or (x%a==0)
    return A and (a>70)


for a in range(1,200):
    if all(f(x) for x in range(1,1000)):
        print(a)