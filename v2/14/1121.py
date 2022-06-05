for i in range(100000):
    x=bin(4**1014-2**i+12)[2:]
    if x.count('0')==2000:
        print(x,i)