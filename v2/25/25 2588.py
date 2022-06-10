def div(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(190201,190260+1):
    b = [i for i in div(x) if i % 2 == 0]
    if len(b)==4:
        print(b[-1],b[-2])
