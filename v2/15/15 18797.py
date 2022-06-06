def f(x,y):
    return (x>a) or (y>x) or (2*y+x<110)


for a in range(20000):
    if all(f(x,y) for x in range(1000) for y in range(1000) ):
        print(a)