count=0
for i in range(1,100000):
    n=bin(i)[2:]
    if int(n)%2==0:
        n=n+bin(sum(list(map(int,[j for j in n]))))[2:]
    else:
        n='1'+n+'00'
    r=int(n,2)
    if 500<=r<=700:
        count+=1
print(count)
