m=100000000000000000000
for i in range(1,10000):
    N=bin(i)[2:]
    if int(N)%2==0:
        N='10'+N+'10'
    else:
        N='1'+N+"00"
    R=int(N,2)
    if R>100:
        m=min(R,m)
print(m)