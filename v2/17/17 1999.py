a=[int(i) for i in open("17_1999.txt")]
n=[]
m=[]
for x in range(len(a)-2):
    if (a[x]%12==0 or a[x+1]%12==0 or a[x+2]%12==0) and (a[x]%3==0 and a[x+1]%3==0 and a[x+2]%3==0):
        n.append((a[x],a[x+1],a[x+2]))
        m.append((a[x]+a[x+1]+a[x+2])/3)
print(len(n),min(m))