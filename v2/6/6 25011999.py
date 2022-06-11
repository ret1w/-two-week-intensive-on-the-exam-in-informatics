m=float('-inf')
for i in range(1,10000000):
    s=i
    s=(s-10)//7
    n=1
    while s>0:
        n*=2
        s=s-n
    if n==1024:
        m=max(i,m)
print(m)