for i in range(1,100000):
    x=i
    Q=8
    P=10
    k1=0
    k2=0
    while x<=100:
        k1+=1
        x=x+P
    while x>=Q:
        k2+=1
        x=x-Q
    l=x+k1
    m=x+k2
    if l==12 and m==19:
        print(i)