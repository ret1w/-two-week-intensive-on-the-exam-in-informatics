count=0
for i in range(100000000000,1000000000000):
    print(i)
    x=i
    a,b,=0,0
    while x>0:
        a+=1
        d=x%10
        if d%3==0:
            b+=d
        x //= 10
    if a==12 and b==99:
        count+=1
        print(count)
