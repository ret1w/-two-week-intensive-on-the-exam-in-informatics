def f(x,n):
    s=''
    while x>0:
        s+=str(x%n)
        x//=n
    return s[::-1]


for n in range(3,100):
    x=f(93,n)
    if x[-1]=="2" and len(x)>=3:
        print(n,x)