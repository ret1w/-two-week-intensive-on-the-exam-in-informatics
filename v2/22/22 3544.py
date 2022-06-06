for i in range(1,10000):
    x=i
    a,b=0,0
    while x>0:
        a+=1
        b+=x%10
        x//=10
    if a==2 and b==10:
        print(i)