def f(x):
    s=''
    while x>0:
        s+=str(x%6)
        x=x//6
    return s[::-1]


for i in range(1000000):
    x=f(36**17-6**i+71)
    if sum(int(i) for i in x) ==61:
        print(i)
        break
