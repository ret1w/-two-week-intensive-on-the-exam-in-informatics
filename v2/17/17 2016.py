a=[int(i) for i in open('17_2016.txt')]
m=[]

for x in a:
    if x%13==7  and x%7!=0 and x%11!=0:
        m.append(x)
print(len(m),max(m)-min(m))