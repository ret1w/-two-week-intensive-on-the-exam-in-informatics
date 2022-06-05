f=list(map(int,open("17 (3).txt",'r+').read().split()))


maxim=0
count=0
for i in range(len(f)):
    for j in range(i,len(f)):
        if (f[i]-f[j])%2==0 and (f[i]*f[j])%36==0:
            maxim=max(maxim,(f[i]+f[j]))
            count+=1
print(count,maxim)
# 3337140 19990
