def f(x,y):
    return (3*x+4*y!=60) or ((a>=x) and (a>=y))


for a in range(0,250):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
        print(a)
        break