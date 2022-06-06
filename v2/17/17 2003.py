a=[int(x) for x in open("17_2003.txt")]
m=[]
for i in range(len(a)):
    if a[i]%3==0 and (a[i]%7!=0 and a[i]%17!=0) and (a[i]%27!=0 and a[i]%19!=0):
        m.append(a[i])
print(len(m),max(m))