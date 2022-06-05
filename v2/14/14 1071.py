def f(x):
    s=''
    while x>0:
        s+=str(x%5)
        x//=5
    return s[::-1]


for i in range(0,1000):
    if f(125**200-5**i+74).count('4')==100:
        print(i)
        break