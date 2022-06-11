a=[int(i) for i in open('17 25011999.txt')]
n=[]
m11=max([j for j in a if j%11==0])
for i in range(len(a)-1):
    if a[i]> m11 or a[i+1] > m11:
        n.append(a[i]+a[i+1])
print(len(n),max(n))
