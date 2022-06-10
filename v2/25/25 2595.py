def div(x):
    d=set()
    for i in range(2,int(x**0.5)):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(400_000_000, 500_000_000):
    p = 1
    if len(div(x)) >= 5:
        for j in div(x)[0:5]:
            p *= j
        if p % 100 == 17 and p <= x:
            print(p, div(x)[4])
