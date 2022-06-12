for i in range(52,10000):
    d=i
    n=50
    s=101
    while n+d<s:
        s+=50
        n-=10
    if n==50:
        print(i)