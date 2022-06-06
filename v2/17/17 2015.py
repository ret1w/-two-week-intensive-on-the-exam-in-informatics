a=[int(i) for i in open('17_2015.txt')]
m=[]

for x in a:
    if (x%10==5 or x%10==7) and x%9!=0 and x%11!=0:
        m.append(x)
print(len(m),min(m)+max(m))