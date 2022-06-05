def f(x):
    s=''
    while x>0:
         s+=str(x%7)
         x//=7
    return s[::-1]


x=51*7**12-7**3-22
f=f(x)
print(sum([int(i) for i in f]))