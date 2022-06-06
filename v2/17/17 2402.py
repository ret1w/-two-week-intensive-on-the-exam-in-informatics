a=[int(i) for i in open("17_2402.txt")]
n=[]
m=[]

for x in range(len(a)-2):
    if a[x]%3==2 or a[x+1]%3==2 or a[x+2]%3==2:
        n.append((a[x],a[x+1],a[x+2]))
        m.append(min(a[x], a[x + 1], a[x + 2]))
print(len(n),sum(m))
