a=[int(i) for i in open("17_37336.txt")]
n=[]
for i in range(len(a)-1):
    if a[i]%3==0 or a[i+1]%3==0:
        n.append(a[i]+a[i+1])
print(len(n),max(n))