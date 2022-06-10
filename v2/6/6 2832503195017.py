for i in range(1,1000000):
    d=i
    n=3
    s=57
    while s<= 1200:
        s=s+d
        n=n+4
    if n==63:
        print(i)