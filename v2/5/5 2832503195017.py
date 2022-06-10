m=0
for i in range(1,100000):
    N=bin(i)[2:]
    if int(N)%2!=0:
        N="1"+N+"0"
    else:
        N="11"+N+"11"
    R=int(N,2)
    if R<126:
        print(R)
        m=max(m,R)
print(m)