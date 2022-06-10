def div(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(300_000,310_000):
    b=[i for i in div(x) if i%3==0 and i!=x]
    if len(b)==5:
        print(x,b[-1])

