a=[int(i) for i in open("17_2401.txt")]
n=[]
m=[]
for i in range(len(a)-1):
     if 50<=abs(a[i])+abs(a[i+1])<=200:
         n.append((a[i],a[i+1]))
         m.append(min(a[i],a[i+1]))
print(len(n),min(m))