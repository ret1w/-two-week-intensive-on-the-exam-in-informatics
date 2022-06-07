for i in range(1,1000):
    N=bin(i)[2:]
    if int(N)%2==0:
        N='10'+N
    else:
        N="1"+N+"10"
    R=int(N,2)
    if R>441:
        print(R,i)
        break