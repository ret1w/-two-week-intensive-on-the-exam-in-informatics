a=[int(i) for i in open("17_job's_07_06_2022.txt")]
n=[]

m21=10000000000
for i in a:
    if i%21==0:
        m21=min(m21,i)

print(m21)

for x in range(len(a)-1):
    if a[x]%m21==0 or a[x+1]%m21==0:
        n.append(a[x]+a[x+1])
print(len(n),max(n))