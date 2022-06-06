a=[int(i) for i in open("17_2238.txt")]
n=[]
m=[]
avg =sum(a)/len(a)

for i in range(len(a)-2):
    if (a[i]>avg and a[i+1]>avg) or (a[i]>avg and a[i+2]>avg) or (a[i+1]>avg and a[i+2]>avg):
        n.append((a[i]+a[i+1]+a[i+2]))
        m.append((a[i],a[i+1],a[i+2]))
print(len(m),max(n))