def f(x):
    s=''
    while x>0:
        s+=str(x%12)
        x=x//12
    return s[::-1]


x=6*144**26+11*12**75-48
f=f(x)
f=f.replace("11","B")
print(f.count("B"))
print(f)