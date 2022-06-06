a=[int(i) for i in open("17_2239.txt")]
m19=0
m=[]
for i in a:
    if i%19==0:
        m19=max(m19,i)

for x in range(len(a)-1):
    if a[x]>m19 or a[x+1]>m19:
        m.append(a[x]+a[x+1])
print(len(m),min(m))