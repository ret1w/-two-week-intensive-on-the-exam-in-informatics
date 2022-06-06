def f(s,c,m):
    if s>=38: return c%2==m%2
    if c==m: return 0
    h=[f(s+1,c+1,m),f(s+2,c+1,m),f(s*2,c+1,m)]
    # return any(h) if (c+1)%2==m%2 else any(h) for 19
    return any(h) if (c+1)%2==m%2 else all(h) # for 20-21


for s in range(1,38):
    for m in range(1,10):
        if f(s,0,m):
            if m==2:print(s,m)
            break