a=[int(i) for i in open("17_2013.txt")]
n=[]
for x in a:
    if (x%10==2 or x%10==7) and x%3==0 and x%11==0:
        n.append(x)
print(len(n),min(n))