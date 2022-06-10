def f(x):
    s=''
    while x>0:
        s+=str(x%5)
        x//=5
    return s[::-1]


x=5**2004-5**1016-25**508-5**400+25**250-27
f=f(x)
print(f)
print(f.count("4"))
