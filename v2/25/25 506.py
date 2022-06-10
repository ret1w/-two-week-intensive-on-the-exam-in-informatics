def prost(x):
    return True if all(x%i!=0 for i in range(2,int(x**0.5)+1)) else False


def div(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(25317,51238):
    b=[i for i in div(x)]
    p=[i for i in b if prost(i)]
    if len(p)>=6:
        print(x,max(p))
