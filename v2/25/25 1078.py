def div(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(1204300,1204380+1):
    b=[i for i in div(x) if i%2==0]
    s = sum(b)
    if s != 0 and s % 10 == 0:
        print(x, s)