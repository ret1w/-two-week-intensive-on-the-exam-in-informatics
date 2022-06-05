def f(x):
    s=''
    while x>0:
        s+=str(x%6)
        x//=6
    return s[::-1]


x=5*216**1156-4*36**1147+6**1153-875
f=f(x)
print(f)
print(f.count('5'))
print(f.count('0'))
print(f.count("5")-f.count("0"))