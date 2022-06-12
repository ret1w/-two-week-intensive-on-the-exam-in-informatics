for i in range(1,10000000000):
    x=i
    l,m=0,0
    while x>12:
        l+=1
        x//=4
    m=x
    if l>m:
        l,m=m,l
    if l==3 and m==7:
        print(i)