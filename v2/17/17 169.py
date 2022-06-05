f=list(map(int,open("17 (3).txt","r+").read().split()))
ans=[i for i in range(len(f)) if f[i]%3==0 and f[i]%7!=0 and  f[i]%17!=0 and f[i]%19!=0 and f[i]%27!=0]
print(len(ans),max(ans))
