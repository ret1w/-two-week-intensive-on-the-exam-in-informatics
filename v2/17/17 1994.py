a=[int(i) for i in open("17_1994.txt")]
m=[]
for x in range(len(a)-1):
    if a[x]*a[x+1]>0 and (a[x]+a[x+1])%7==0:
        m.append(a[x]*a[x+1])
print(len(m),min(m))