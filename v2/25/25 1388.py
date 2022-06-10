def div(x):
    d=set()
    for i in range(2,int(x**0.5)):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for i in range(150000,151000):
    s=sum(div(i))
    if s%13==10:
        print(i,s)
