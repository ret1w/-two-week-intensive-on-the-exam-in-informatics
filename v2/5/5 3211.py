for i in range(10000):
    N=bin(i)[2:]
    if int(N)%2==0:
        N=N+"10"
    else:
        N="1"+N+"01"
    R=int(N,2)
    if R>516:
        print(R,i)
        break