def f(s,c,m):
    if s==0: return c%2==m%2
    h=[f((s+1)//2,c+1,m)]
    if s>0: h+=[f(s-1,c+1,m)]
    if c==m: return 0
    return any(h) if (c+1)%2==m%2 else all(h)


for s in range(10,100):
    for m in range(1,5):
        if f(s,0,m):
            print(s,m)
            break
