def div(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(55_0000,56_0000):
    d=[i for i in div(x) if i%10==7 and i!=x]
    if len(d)==3:
        print(x,d[-1])
