def f(x,y):
    return (2*x+3*y>30) or (x+y<=a)

for a in range(0,1150):
    if all(f(x,y) for x in range(100) for y in range(1000)):
        print(a)