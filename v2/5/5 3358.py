for i in range(1000):
    N=bin(i)[2:]
    if N.count("1")%2==0:
        N="1"+N+"00"
    else:
        N="11"+N
    R=int(N,2)
    if R>=412:
        print(R,i)
        break
