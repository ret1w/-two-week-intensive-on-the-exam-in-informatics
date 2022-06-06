f="".join([i for i in open("24 33196.txt")])
a="ZXCVBNMSDFGHJKLQWERTYUIOP"
n=[]
for x in range(len(f)):
    if f[x] =="A" and f[x+1] in a:
        n.append(f[x+1])
m=-100
l=''
for i in a:
    if n.count(l)<n.count(i):
        l=i
        m=max(m,n.count(i))
print(m,l)


