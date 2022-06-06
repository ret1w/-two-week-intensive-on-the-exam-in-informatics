a=[int(i) for i in open("17-2017.txt")]
n=[]
for x in a:
    if x%16==11 and x%7==0 and x%6!=0 and x%13!=0 and x%19!=0:
        n.append(x)
print(sum(n),len(n))