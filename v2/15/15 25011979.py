def f(x):
    return ((x%2==0)<=(not(x%5==0))) or (x + a>=90)


for a in range(1,200):
    if all(f(x) for x in range(1,100)):
        print(a)
        break