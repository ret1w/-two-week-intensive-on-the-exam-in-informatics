def prost(x):
    return True if all(x%i!=0 for i in range(2,int(x**0.5)+1)) else False


for x in range(608_0068,608_0176+1):
    if prost(x):
        print(x)