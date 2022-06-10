a=[int(i) for i in open("17 2832503195017.txt")]
n=[]

m=-1
for i in a:
    if i%111==0:
        m=max(i,m)
print(m)
for i in range(len(a)-1):
    if a[i]>m or a[i+1]>m:
        if a[i]%10==7 or a[i+1]%10==7:
            n.append(a[i]+a[i+1])
print(n)
print(len(n),min(n))