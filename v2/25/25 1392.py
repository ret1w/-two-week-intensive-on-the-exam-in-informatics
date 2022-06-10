def div(x):
    d=set()
    for i in range(2,int(x**0.5)):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(550000,555000):
    try:
        f=sum(div(x))//len(div(x))
        if f%31==13:
            print(x,f)
    except:
        ...
