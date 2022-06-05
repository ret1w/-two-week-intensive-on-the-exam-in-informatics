def f(a,b,c,m):
    if a+b>=44: return c%2==m%2
    if c==m: return 0
    h=[f(a+b,b,c+1,m),f(a,b+a,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)


for b in range(1,100):
    for m in range(1,10):
        if f(11,b,0,m):
            if m==3:print(b,m)
            break
