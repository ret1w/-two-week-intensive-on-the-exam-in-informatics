def f(a,b,c,m):
    if a+b>=231: return c%2==m%2
    if c==m: return 0

    h=[f(a*2,b,c+1,m),f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)


for b in range(1,214):
    for m in range(1,10):
        if f(17,b,0,m):
            if m==4:print(b,m)
            break