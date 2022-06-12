def f(x):
    s=''
    while x>0:
        s+=str(x%5)
        x//=5
    return s[::-1]


x=25**94+5**216-125
print(f(x))
print(f(x).count('4'))