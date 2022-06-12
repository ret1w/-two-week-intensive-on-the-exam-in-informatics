def f(x):
    s=''
    while x>0:
        s+=str(x%9)
        x//=9
    return s[::-1]


a=[i*2 for i in "0123456789"]
n=[]

for x in range(1000000,9999999+1):
    d=f(x)
    if d[0]!="0" and d[0]!="3" and d[0]!="7":
        for j in a:
            if j in d:
                break
        else:
            print(d)
            n.append(d)
print(len(n))
