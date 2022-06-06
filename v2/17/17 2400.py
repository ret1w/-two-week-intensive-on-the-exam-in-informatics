a=[int(i) for i in open("17_2400.txt")]
m=[]
n=[]
for i in range(len(a)-1):
    if a[i]+a[i+1]>100 and (a[i]<0 or a[i+1]<0):
        m.append((a[i],a[i+1]))
        n.append(a[i]*a[i+1])
print(len(m),max(n))