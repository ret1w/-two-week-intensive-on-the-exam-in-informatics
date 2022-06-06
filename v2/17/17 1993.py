a=[int(i) for i in open("17 1993.txt")]
n=[]
for x in range(len(a)-1):
    if  (a[x]+a[x+1])%3==0 and  (a[x]+a[x+1])%6!=0 and abs((a[x]*a[x+1]))%10==8:
        n.append( (a[x]+a[x+1]))
print(len(n),max(n))