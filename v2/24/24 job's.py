a=''.join([i for i in open("24_jobs's.txt") ])
a=a.replace("AB","*").replace("CB","*")
for x in "ABC":
    a=a.replace(x," ")
a=list(map(str,a.split()))
print(len(max(a,key=len)))