for i in range(0,2**31):
    x = i
    a = 0
    b = 0
    while x > 0:
        c = x % 2
        if c == 0:
            a += 1
        else:
            b += 1
        x = x // 10
    if a==3 and b==2:
        print(i)
        break