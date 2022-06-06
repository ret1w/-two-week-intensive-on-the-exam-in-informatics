def f(x):
    return (x&85==0)<=((x&54!=0)<=(x&a!=0))


for a in range(200):
    if all(f(x) for x in range(15000)):
        print(a)