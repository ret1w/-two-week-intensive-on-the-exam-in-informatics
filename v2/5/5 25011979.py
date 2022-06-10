for i in range(1,100):
    N=bin(i)[2:]
    for _ in range(3):
        if N.count("0")==N.count("1"):
            N+=N[-1]
        else:
            if N.count("0") < N.count("1"):
                N+="0"
            else:
                N+="1"
    R=int(N,2)
    if R%4==0 and R%8!=0:
        print(i)