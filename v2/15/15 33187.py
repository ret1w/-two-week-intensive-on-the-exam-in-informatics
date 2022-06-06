def f(x):
    return (90%a==0) and ( (x%a!=0) <= ((x%15==0) <=  (x%20!=0)) )


for a in range(1,200):
    if all(f(x) for x in range(100)):
        print(a)