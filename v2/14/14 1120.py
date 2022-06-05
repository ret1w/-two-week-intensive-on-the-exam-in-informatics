for i in range(10000):
    if bin(4**2015+2**i-2**2015+15)[2:].count('1')==500:
        print(i)