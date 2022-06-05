def f(x):
    s=''
    while x>0:
        s+=str(x%3)
        x//=3
    return s[::-1]


x=2*27**7+3**10-9
print(f(x))
print(f(x).count('0'))