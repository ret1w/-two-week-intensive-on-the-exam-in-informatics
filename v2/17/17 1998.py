a=[int(i) for i in open("17_1998.txt")]
n=[]

for x in range(len(a)-2):
    if (a[x]*a[x+1]*a[x+2])%7==0 and abs((a[x]+a[x+1]+a[x+2]))%10==5:
        n.append((a[x]+a[x+1]+a[x+2]))
print(len(n),max(n))