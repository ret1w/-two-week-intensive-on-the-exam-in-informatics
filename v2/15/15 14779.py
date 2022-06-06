def f(x,y):
    return ((x<5)<=(x**2<a)) and ((y**2<=a)<=(y<=5))

n=[]
for a in range(0,1000):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
        n.append(a)
print(len(n))

