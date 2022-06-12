a=[int(i) for i in open("17 25006980.txt")]
n=[]

for i in range(len(a)-1):
    if (a[i]+a[i+1])%3==0 and (a[i]+a[i+1])%6!=0 and abs(a[i]*a[i+1])%10==8:
        n.append(a[i]+a[i+1])
print(len(n),max(n))