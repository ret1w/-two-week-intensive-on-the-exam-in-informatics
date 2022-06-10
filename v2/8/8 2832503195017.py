def f(x):
    s=''
    while x>0:
        s+=str(x%9)
        x//=9
    return s[::-1]


count=0
a=[str(g)*3 for g in range(0,10)]


for i in range(1000000,9999999+1):
        d=f(i)
        if d[-1] != '3' and d[-1]!="4" and d[-1]!="7":
            for j in a:
                if j in d:
                    break
            else:
                count = +1
print(count)
