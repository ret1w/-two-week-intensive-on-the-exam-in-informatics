def f(x):
    s=''
    while x>0:
        s+=str(x%3)
        x//=3
    return s[::-1]


for x in range(20,31):
    print(x,f(x))