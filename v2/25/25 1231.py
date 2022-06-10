def div(x):
    d=set()
    for i in range(2,int(x**0.5)):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(250200,251200):
    if len(div(x))>=2:
        s=div(x)[-1]+div(x)[0]
        if s%123==17:
            print(x,s)
