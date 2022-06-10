f=[int(i) for i in open("17 (3).txt")]
n=[]

m11=-10000000000000000000000000
for i in range(len(f)):
    if f[i]%11==0:
        m11=max(f[i],m11)
print(m11)


for i in range(len(f)-1):
    if f[i]%11==0 or f[i+1]%11==0:
        if f[i]+f[i+1]<=m11:
            n.append(f[i]+f[i+1])
print(len(n),max(n))

