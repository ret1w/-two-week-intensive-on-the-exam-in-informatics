for i in range(1,10000):
    x=i
    L,M=0,0
    while x>0:
        M=M+1
        if x%2!=0:
            L=L+1
        x//=2
    if L==5 and M==8:
        print(i)
        break